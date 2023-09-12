from .models import  Books, Bookinventory, NewPricingModel, Donationreqs, Users
from django.http import JsonResponse
from django.db import connection
import json
from django.http import HttpResponse
import collections


# for /product link
def all_books(request,pg):
	#print (pg)
	start= (int(pg)-1)*10 # starting page number offset, when taking 10 entries per page
	cursor = connection.cursor()
	cursor.execute(''' SELECT book_id, title, thumb, price, slug FROM books ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)
	rows = [x for x in cursor]
	print (rows)
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)


# for /product/<slug:slug> link

# fetching common product details
def product_details(request, slug):
	product_json= {}
	cursor = connection.cursor()
	cursor.execute (''' SELECT book_id, title, thumb, price, slug, publication, publication_date, language, binding, weight, no_of_pages, edition, isbn, author, book_desc, is_out_of_stack FROM books 
						WHERE slug= %s''', slug)
	common_data_row= [x for x in cursor][0]
	common_data_cols = [x[0] for x in cursor.description]
	common_data_dict= {}
	for i in range(0, len(common_data_cols)-1):
		common_data_dict[common_data_cols[i]]= common_data_row[i]
	product_json["product_details"]= common_data_dict
	product_book_id= common_data_row[0]
	product_stock_status= common_data_row[len(common_data_cols)-1]
	#print (product_stock_status)
	#print (product_book_id) 
	#print (product_json)

	if (product_stock_status== "Y"):
		product_json["product_condition"]= {}
		product_json["product_condition"]["shipping"]= "N/A"
		product_json["product_condition"]["is_soldout"]= "Y"
		#print (product_json)
		product_json= json.dumps(product_json)
		return HttpResponse(product_json)

	else:
		product_json["product_condition"]= product_condition(product_book_id)
		product_json= json.dumps(product_json)
		return HttpResponse(product_json)
		

# fetching product condition & donor details
def product_condition(product_id):
	product_condition= {}
	cursor = connection.cursor()
	cursor.execute('''UPDATE bookinventory SET book_condition = REPLACE(book_condition, "Â", "")''')
	cursor.execute('''UPDATE bookinventory SET book_condition = REPLACE(book_condition, " ", "")''')
	cursor.execute (''' SELECT book_condition, book_inv_id FROM bookinventory WHERE book_id= %s AND is_soldout= "N" ''', product_id)
	
	# this is making API slow
	book_inv_dict= {}
	book_map= [x for x in cursor]
	for k,v in book_map:
		book_inv_dict.setdefault(k,[]).append(v)
	#print (book_inv_dict)

	book_condition_set= book_inv_dict.keys()
	#print (book_condition_set)

	for each_condition in book_condition_set:
		product_condition[each_condition]= {}
		cursor.execute (''' SELECT rack_no, donation_req_id, book_inv_id FROM bookinventory WHERE book_condition= %s AND book_id= %s AND is_soldout= "N" ORDER BY i_date LIMIT 1''', (each_condition, product_id))
		condition_row_1= [x for x in cursor][0]
		#print (condition_row_1)

		condition_rack_no= condition_row_1[0]
		#print (condition_rack_no)

		condition_donation_id= int(condition_row_1[1])
		#print (condition_donation_id)

		condition_book_inv_id= int(condition_row_1[2])
		#print (condition_book_inv_id)

		cursor.execute (''' SELECT new_price FROM new_pricing_model WHERE book_inv_id= %s''', condition_book_inv_id)
		condition_new_price= [x[0] for x in cursor]
		#print (condition_new_price)

		if (len(condition_new_price)==0):
			#print ("no pricing model exists")
			condition_new_price= "NA"
			product_condition[each_condition]["shipping"]= condition_new_price

		else:
			condition_new_price= condition_new_price[0]
			#print ("data fetched")
			product_condition[each_condition]["shipping"]= condition_new_price

		cursor.execute (''' SELECT donor_name, user_id FROM donationreqs WHERE donation_req_id= %s''', condition_donation_id)
		condition_row_2= [x for x in cursor][0]
		#print (condition_row_2)

		condition_donor_name= condition_row_2[0]
		#print (condition_donor_name)

		condition_user_id= condition_row_2[1]
		#print (condition_user_id)

		cursor.execute (''' SELECT avatar FROM users WHERE id= %s''', condition_user_id)
		condition_user_image= [x[0] for x in cursor][0]
		#print(condition_user_image)

		product_condition[each_condition]["book_inv_id"]= condition_book_inv_id
		product_condition[each_condition]["rack_no"]= condition_rack_no
		product_condition[each_condition]["donor_name"]= condition_donor_name
		product_condition[each_condition]["avatar"]= condition_user_image
		product_condition[each_condition]["total_qty"]= len(book_inv_dict[each_condition])
		product_condition[each_condition]["book_inv_id's"]= book_inv_dict[each_condition]


	return product_condition
