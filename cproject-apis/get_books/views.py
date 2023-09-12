from .models import  Books, Categories
from django.core import serializers
from django.http import JsonResponse
from django.db import connection
import json
from django.http import HttpResponse


# for /category link
def all_books(request,pg):
	start= (int(pg)-1)*10
	#print (pg)
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



#---------------------------------------------------------------------------------------------
# COMPETITIVE EXAMS 
#---------------------------------------------------------------------------------------------



# for /category/competitive-exams link
# category id= 187
def competitive_exams(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug from 
						(SELECT * FROM books WHERE category = 187 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 187) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 187)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




#---------------------------------------------------------------------------------------------
# COMPETITIVE EXAMS > CAT & its sub-categories
#---------------------------------------------------------------------------------------------



# for /category/competitive-exams/cat link
# category id= 361
def competitive_cat(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 361 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 361) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 361)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	



#---------------------------------------------------------------------------------------------
# COMPETITIVE EXAMS > ENGINEERING & MEDICAL & its sub-categories
#---------------------------------------------------------------------------------------------



# for /category/competitive-exams/engineering link
# category id= 190
def competitive_engg(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 190 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 190) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 190)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	




# for /category/competitive-exams/engineering/aieee
# category id= 194
def engg_aieee(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 194 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 194) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 194)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/competitive-exams/engineering/engineering-post-graduate
# category id= 195
def engg_postgrad(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 195 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 195) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 195)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/competitive-exams/engineering/iit
# category id= 196
def engg_iit(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 196 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 196) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 196)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	




# for /category/competitive-exams/engineering/medical
# category id= 342
def engg_medical(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 342 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 342) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 342)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	




# for /category/competitive-exams/engineering/others
# category id= 198
def engg_others(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 198 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 198) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 198)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/competitive-exams/engineering/state-level
# category id= 197
def engg_statelevel(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 197 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 197) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 197)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	



#---------------------------------------------------------------------------------------------
# COMPETITIVE EXAMS > GENERAL KNOWLEDGE & LEARNING & its sub-categories
#---------------------------------------------------------------------------------------------	



# for /category/competitive-exams/general-knowledge-learni
# category id= 352
def competitive_gk(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 352 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 352) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 352)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	




# for /category/competitive-exams/general-knowledge-learni/dic
# category id= 354
def gk_dict(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 354 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 354) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 354)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	




# for /category/competitive-exams/general-knowledge-learni/gk
# category id= 353
def gk_gk(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 353 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 353) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 353)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	



#---------------------------------------------------------------------------------------------
# COMPETITIVE EXAMS > GOVERNMENT JOBS & its sub-categories
#---------------------------------------------------------------------------------------------	



# for /category/competitive-exams/government-jobs
# category id= 191
def competitive_govtjobs(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 191 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 191) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 191)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/competitive-exams/government-jobs/banking
# category id= 199
def govtjobs_banking(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 199 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 199) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 199)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/competitive-exams/government-jobs/others
# category id= 205
def govtjobs_others(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 205 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 205) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 205)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/competitive-exams/government-jobs/railway
# category id= 201
def govtjobs_railway(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 201 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 201) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 201)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/competitive-exams/government-jobs/ssc
# category id= 202
def govtjobs_ssc(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 202 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 202) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 202)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/competitive-exams/government-jobs/teaching-related-exams
# category id= 203
def govtjobs_teachingexams(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 203 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 203) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 203)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/competitive-exams/government-jobs/upsc
# category id= 204
def govtjobs_upsc (request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 204 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 204) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 204)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)



#---------------------------------------------------------------------------------------------
# COMPETITIVE EXAMS > INTERNATIONAL EXAMS & its sub-categories
#---------------------------------------------------------------------------------------------	



# for /category/competitive-exams/international-exams
# category id= 192
def competitive_internationalexams(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 192 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 192) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 192)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	




# for /category/competitive-exams/international-exams/gmat
# category id= 206
def internationalexams_gmat(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 206 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 206) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 206)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	




# for /category/competitive-exams/international-exams/gre
# category id= 207
def internationalexams_gre(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 207 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 207) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 207)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/competitive-exams/international-exams/others
# category id= 210
def internationalexams_others(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 210 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 210) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 210)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/competitive-exams/international-exams/sat
# category id= 209
def internationalexams_sat(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 209 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 209) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 209)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)			



#---------------------------------------------------------------------------------------------
# COMPETITIVE EXAMS > SCHOOL LEVEL & its sub-categories
#---------------------------------------------------------------------------------------------	



# for /category/competitive-exams/school-level
# category id= 193
def competitive_schoollevel(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 193 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 193) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 193)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/competitive-exams/school-level/navodaya-vidyalaya
# category id= 211
def schoollevel_navodaya(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 211 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 211) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 211)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/competitive-exams/school-level/ntse
# category id= 212
def schoollevel_ntse(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 212 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 212) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 212)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/competitive-exams/school-level/olympiads
# category id= 213
def schoollevel_olympiads(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 213 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 213) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 213)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/competitive-exams/school-level/others
# category id= 215
def schoollevel_others(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 215 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 215) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 215)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/competitive-exams/school-level/sainik-school
# category id= 214
def schoollevel_sainik(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 214 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 214) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 214)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	



#---------------------------------------------------------------------------------------------
# FICTION NON-FICTION
#---------------------------------------------------------------------------------------------



# for /category/fiction-non-fiction link
# category id= 216
def fiction_and_nonfiction(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 216 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 216) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 216)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




#---------------------------------------------------------------------------------------------
# FICTION NON-FICTION > FICTION & its sub-categories
#---------------------------------------------------------------------------------------------



# for /category/fiction-non-fiction/fiction link
# category id= 217
def fiction_and_nonfiction__fiction(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 217 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 217) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 217)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/fiction-non-fiction/fiction/comics-graphic-novel link
# category id= 218
def fiction_and_nonfiction__fiction_comics(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 218 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 218) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 218)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/fiction-non-fiction/fiction/drama link
# category id= 219
def fiction_and_nonfiction__fiction_drama(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 219 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 219) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 219)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/fiction-non-fiction/fiction/horror-and-thriller link
# category id= 220
def fiction_and_nonfiction__fiction_horrorthriller(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 220 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 220) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 220)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/fiction-non-fiction/fiction/humour link
# category id= 221
def fiction_and_nonfiction__fiction_humour(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 221 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 221) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 221)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/fiction-non-fiction/fiction/literary link
# category id= 222
def fiction_and_nonfiction__fiction_literary(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 222 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 222) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 222)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/fiction-non-fiction/fiction/mystery link
# category id= 223
def fiction_and_nonfiction__fiction_mystery(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 223 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 223) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 223)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/fiction-non-fiction/fiction/romance link
# category id= 224
def fiction_and_nonfiction__fiction_romance(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 224 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 224) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 224)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/fiction-non-fiction/fiction/science-fiction link
# category id= 225
def fiction_and_nonfiction__fiction_sciencefiction(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 225 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 225) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 225)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/fiction-non-fiction/fiction/short-stories link
# category id= 226
def fiction_and_nonfiction__fiction_shortstories(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 226 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 226) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 226)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/fiction-non-fiction/fiction/teens link
# category id= 227
def fiction_and_nonfiction__fiction_teens(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 227 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 227) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 227)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




#---------------------------------------------------------------------------------------------
# FICTION NON-FICTION > FICTION & NON FICTION OTHERS & its sub-categories
#---------------------------------------------------------------------------------------------



# for /category/fiction-non-fiction/fiction-non-fiction-others link
# category id= 244
def fiction_and_nonfiction__others(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 244 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 244) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 244)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/fiction-non-fiction/fiction-non-fiction-others/astrology link
# category id= 245
def fiction_and_nonfiction__others_astrology(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 245 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 245) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 245)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/fiction-non-fiction/fiction-non-fiction-others/business-management link
# category id= 247
def fiction_and_nonfiction__others_businessmgmt(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 247 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 247) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 247)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/fiction-non-fiction/fiction-non-fiction-others/health link
# category id= 248
def fiction_and_nonfiction__others_health(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 248 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 248) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 248)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/fiction-non-fiction/fiction-non-fiction-others/history-and-politics link
# category id= 249
def fiction_and_nonfiction__others_history(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 249 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 249) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 249)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/fiction-non-fiction/fiction-non-fiction-others/others link
# category id= 251
def fiction_and_nonfiction__others_others(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 251 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 251) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 251)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/fiction-non-fiction/fiction-non-fiction-others/sports-games link
# category id= 250
def fiction_and_nonfiction__others_sportgames(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 250 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 250) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 250)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




#---------------------------------------------------------------------------------------------
# FICTION NON-FICTION > MOTIVATION & SELF-HELP & its sub-categories
#---------------------------------------------------------------------------------------------



# for /category/fiction-non-fiction/motivation-self-help link
# category id= 350
def fiction_and_nonfiction__motivationselfhelp(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 350 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 350) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 350)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




#---------------------------------------------------------------------------------------------
# FICTION NON-FICTION > NON FICTION & its sub-categories
#---------------------------------------------------------------------------------------------



# for /category/fiction-non-fiction/non-fiction link
# category id= 228
def fiction_and_nonfiction__nonfiction(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 228 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 228) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 228)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/fiction-non-fiction/non-fiction/biographies link
# category id= 229
def fiction_and_nonfiction__nonfiction_biographies(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 229 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 229) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 229)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/fiction-non-fiction/non-fiction/coffee-table link
# category id= 230
def fiction_and_nonfiction__nonfiction_coffeetable(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 230 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 230) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 230)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/fiction-non-fiction/non-fiction/computer-and-internet link
# category id= 231
def fiction_and_nonfiction__nonfiction_computer(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 231 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 231) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 231)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/fiction-non-fiction/non-fiction/cooking link
# category id= 232
def fiction_and_nonfiction__nonfiction_cooking(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 232 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 232) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 232)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/fiction-non-fiction/non-fiction/entertainment link
# category id= 233
def fiction_and_nonfiction__nonfiction_entertainment(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 233 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 233) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 233)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/fiction-non-fiction/non-fiction/househome link
# category id= 234
def fiction_and_nonfiction__nonfiction_househome(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 234 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 234) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 234)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/fiction-non-fiction/non-fiction/pets link
# category id= 366
def fiction_and_nonfiction__nonfiction_pets(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 366 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 366) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 366)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/fiction-non-fiction/non-fiction/photography link
# category id= 235
def fiction_and_nonfiction__nonfiction_photography(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 235 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 235) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 235)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/fiction-non-fiction/non-fiction/sports link
# category id= 236
def fiction_and_nonfiction__nonfiction_sports(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 236 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 236) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 236)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/fiction-non-fiction/non-fiction/travel link
# category id= 237
def fiction_and_nonfiction__nonfiction_travel(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 237 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 237) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 237)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




#---------------------------------------------------------------------------------------------
# FICTION NON-FICTION > RELIGION & SPIRITUALITY & its sub-categories
#---------------------------------------------------------------------------------------------



# for /category/fiction-non-fiction/religion-spirituality link
# category id= 238
def fiction_and_nonfiction__religion(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 238 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 238) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 238)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/fiction-non-fiction/religion-spirituality/holy-books link
# category id= 239
def fiction_and_nonfiction__religion_holybooks(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 239 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 239) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 239)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/fiction-non-fiction/religion-spirituality/others link
# category id= 243
def fiction_and_nonfiction__religion_others(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 243 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 243) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 243)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/fiction-non-fiction/religion-spirituality/philosophy link
# category id= 240
def fiction_and_nonfiction__religion_philosophy(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 240 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 240) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 240)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/fiction-non-fiction/religion-spirituality/religions link
# category id= 241
def fiction_and_nonfiction__religion_religions(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 241 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 241) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 241)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/fiction-non-fiction/religion-spirituality/spirituality link
# category id= 242
def fiction_and_nonfiction__religion_spirituality(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 242 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 242) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 242)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	



#---------------------------------------------------------------------------------------------
# NOTEBOOK
#---------------------------------------------------------------------------------------------



# for /category/note-book- link
# category id= 362
def notebook(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 362 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 362) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 362)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	




#---------------------------------------------------------------------------------------------
# SCHOOL & CHILDREN BOOKS
#---------------------------------------------------------------------------------------------



# for /category/school-children-books link
# category id= 252
def schoolchildren(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 252 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 252) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 252)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	




#---------------------------------------------------------------------------------------------
# SCHOOL & CHILDREN BOOKS > CHILDREN BOOKS & its sub-categories
#---------------------------------------------------------------------------------------------



# for /category/school-children-books/children-books link
# category id= 253
def schoolchildren_children(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 253 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 253) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 253)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/school-children-books/children-books/action-and-adventure link
# category id= 256
def schoolchildren_children_action(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 256 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 256) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 256)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/school-children-books/children-books/activity-books link
# category id= 257
def schoolchildren_children_activitybooks(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 257 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 257) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 257)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/school-children-books/children-books/childrens-literature link
# category id= 258
def schoolchildren_children_literature(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 258 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 258) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 258)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/school-children-books/children-books/comics-graphic-novels
# category id= 259
def schoolchildren_children_comics(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 259 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 259) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 259)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/school-children-books/children-books/disney-store
# category id= 260
def schoolchildren_children_disneystore(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 260 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 260) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 260)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/school-children-books/children-books/fun-humour
# category id= 261
def schoolchildren_children_funhumour(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 261 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 261) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 261)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/school-children-books/children-books/history-mythology-
# category id= 262
def schoolchildren_children_mythology(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 262 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 262) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 262)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/school-children-books/children-books/knowledge-and-learning
# category id= 263
def schoolchildren_children_knowledge(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 263 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 263) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 263)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/school-children-books/children-books/others
# category id= 265
def schoolchildren_children_others(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 265 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 265) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 265)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/school-children-books/children-books/picture-book
# category id= 264
def schoolchildren_children_picturebook(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 264 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 264) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 264)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




#---------------------------------------------------------------------------------------------
# SCHOOL & CHILDREN BOOKS > CLASSES & its sub-categories
#---------------------------------------------------------------------------------------------



# for /category/school-children-books/classes link
# category id= 266
def schoolchildren_classes (request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 266 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 266) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 266)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/school-children-books/classes/kg link
# category id= 267
def schoolchildren_classes_kg(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 267 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 267) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 267)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/school-children-books/classes/class-1 link
# category id= 268
def schoolchildren_classes_class1(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 268 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 268) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 268)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/school-children-books/classes/class-2 link
# category id= 269
def schoolchildren_classes_class2(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 269 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 269) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 269)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	




# for /category/school-children-books/classes/class-3 link
# category id= 270
def schoolchildren_classes_class3(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 270 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 270) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 270)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	




# for /category/school-children-books/classes/class-4 link
# category id= 271
def schoolchildren_classes_class4(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 271 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 271) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 271)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	




# for /category/school-children-books/classes/class-5 link
# category id= 272
def schoolchildren_classes_class5(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 272 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 272) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 272)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	




# for /category/school-children-books/classes/class-6 link
# category id= 273
def schoolchildren_classes_class6(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 273 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 273) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 273)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	




# for /category/school-children-books/classes/class-7 link
# category id= 274
def schoolchildren_classes_class7(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 274 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 274) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 274)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	




# for /category/school-children-books/classes/class-8 link
# category id= 275
def schoolchildren_classes_class8(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 275 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 275) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 275)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	




# for /category/school-children-books/classes/class-9 link
# category id= 276
def schoolchildren_classes_class9(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 276 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 276) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 276)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/school-children-books/classes/class-10 link
# category id= 277
def schoolchildren_classes_class10(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 277 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 277) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 277)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	




# for /category/school-children-books/classes/class-11 link
# category id= 278
def schoolchildren_classes_class11(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 278 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 278) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 278)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	




# for /category/school-children-books/classes/class-12 link
# category id= 279
def schoolchildren_classes_class12(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 279 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 279) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 279)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)
	



#---------------------------------------------------------------------------------------------
# SCHOOL & CHILDREN BOOKS > NCERT & its sub-categories
#---------------------------------------------------------------------------------------------



# for /category/school-children-books/ncert link
# category id= 280
def schoolchildren_ncert (request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 280 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 280) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 280)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)



# for /category/school-children-books/ncert/class-6 link
# category id= 281
def schoolchildren_ncert_class6(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 281 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 281) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 281)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)



# for /category/school-children-books/ncert/class-7 link
# category id= 282
def schoolchildren_ncert_class7(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 282 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 282) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 282)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)



# for /category/school-children-books/ncert/class-8 link
# category id= 283
def schoolchildren_ncert_class8(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 283 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 283) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 283)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	



# for /category/school-children-books/ncert/class-9 link
# category id= 284
def schoolchildren_ncert_class9(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 284 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 284) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 284)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	



# for /category/school-children-books/ncert/class-10 link
# category id= 285
def schoolchildren_ncert_class10(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 285 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 285) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 285)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	



# for /category/school-children-books/ncert/class-11 link
# category id= 286
def schoolchildren_ncert_class11(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 286 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 286) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 286)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)



# for /category/school-children-books/ncert/class-12 link
# category id= 287
def schoolchildren_ncert_class12(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 287 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 287) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 287)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)
	



#---------------------------------------------------------------------------------------------
# SCHOOL & CHILDREN BOOKS > DICTIONARY LEVEL & its sub-categories
#---------------------------------------------------------------------------------------------



# for /category/school-children-books/dictionary-level- link
# category id= 355
def schoolchildren_dictionary (request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 355 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 355) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 355)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)



# for /category/school-children-books/dictionary-level-/english-to-english- link
# category id= 357
def schoolchildren_dictionary_engtoeng(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 357 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 357) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 357)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)



# for /category/school-children-books/dictionary-level-/english-to-hindi- link
# category id= 358
def schoolchildren_dictionary_engtohindi(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 358 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 358) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 358)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)



# for /category/school-children-books/dictionary-level-/foreign-language link
# category id= 365
def schoolchildren_dictionary_foreign(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 365 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 365) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 365)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	



# for /category/school-children-books/dictionary-level-/hindi-to-english- link
# category id= 359
def schoolchildren_dictionary_hintoeng(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 359 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 359) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 359)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	



# for /category/school-children-books/dictionary-level-/subject-wise- link
# category id= 356
def schoolchildren_dictionary_subjectwise(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 356 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 356) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 356)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	




#---------------------------------------------------------------------------------------------
# UNIVERSITY BOOKS
#---------------------------------------------------------------------------------------------



# for /category/university-books link
# category id= 303
def university(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 303 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 303) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 303)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	



#---------------------------------------------------------------------------------------------
# UNIVERSITY BOOKS > ENGINEERING & its sub-categories
#---------------------------------------------------------------------------------------------



# for /category/university-books/engineering link
# category id= 304
def university_engg(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 304 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 304) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 304)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/university-books/engineering/aeronautical link
# category id= 305
def university_engg_aeronautical(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 305 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 305) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 305)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/university-books/engineering/bio-technology link
# category id= 306
def university_engg_biotechnology(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 306 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 306) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 306)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/university-books/engineering/chemical- link
# category id= 307
def university_engg_chemical(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 307 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 307) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 307)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/university-books/engineering/civil- link
# category id= 308
def university_engg_civil(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 308 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 308) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 308)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/university-books/engineering/computer-science link
# category id= 309
def university_engg_computersci(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 309 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 309) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 309)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/university-books/engineering/electrical- link
# category id= 310
def university_engg_electrical(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 310 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 310) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 310)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/university-books/engineering/electronics link
# category id= 311
def university_engg_electronics(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 311 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 311) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 311)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	




# for /category/university-books/engineering/marine link
# category id= 312
def university_engg_marine(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 312 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 312) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 312)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)		




# for /category/university-books/engineering/mechanical link
# category id= 313
def university_engg_mechanical(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 313 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 313) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 313)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	




# for /category/university-books/engineering/others link
# category id= 314
def university_engg_others(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 314 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 314) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 314)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)		



#---------------------------------------------------------------------------------------------
# UNIVERSITY BOOKS > FINANCE & its sub-categories
#---------------------------------------------------------------------------------------------



# for /category/university-books/finance link
# category id= 360
def university_finance(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 360 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 360) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 360)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)



#---------------------------------------------------------------------------------------------
# UNIVERSITY BOOKS > MEDICAL & its sub-categories
#---------------------------------------------------------------------------------------------



# for /category/university-books/medical link
# category id= 315
def university_medical(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 315 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 315) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 315)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/university-books/medical/ayurveda link
# category id= 316
def university_medical_ayurveda(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 316 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 316) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 316)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/university-books/medical/dental link
# category id= 317
def university_medical_dental(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 317 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 317) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 317)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/university-books/medical/mbbs link
# category id= 318
def university_medical_mbbs(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 318 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 318) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 318)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	




# for /category/university-books/medical/others link
# category id= 321
def university_medical_others(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 321 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 321) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 321)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	




# for /category/university-books/medical/pg link
# category id= 319
def university_medical_pg(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 319 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 319) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 319)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	




# for /category/university-books/medical/pharmacy link
# category id= 320
def university_medical_pharmacy(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 320 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 320) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 320)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	



#---------------------------------------------------------------------------------------------
# UNIVERSITY BOOKS > OTHERS & its sub-categories
#---------------------------------------------------------------------------------------------



# for /category/university-books/others link
# category id= 329
def university_others(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 329 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 329) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 329)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/university-books/others/bba link
# category id= 330
def university_others_bba(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 330 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 330) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 330)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/university-books/others/bcom link
# category id= 331
def university_others_bcom(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 331 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 331) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 331)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/university-books/others/law link
# category id= 332
def university_others_law(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 332 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 332) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 332)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/university-books/others/mba link
# category id= 333
def university_others_mba(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 333 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 333) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 333)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/university-books/others/mcom link
# category id= 334
def university_others_mcom(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 334 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 334) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 334)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/university-books/others/others link
# category id= 336
def university_others_others(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 336 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 336) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 336)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/university-books/others/phd link
# category id= 335
def university_others_phd(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 335 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 335) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 335)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/university-books/others/probability-statistics link
# category id= 343
def university_others_stats(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 343 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 343) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 343)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)



#---------------------------------------------------------------------------------------------
# UNIVERSITY BOOKS > SCIENCE & ARTS & its sub-categories
#---------------------------------------------------------------------------------------------



# for /category/university-books/science-arts link
# category id= 322
def university_sciencearts(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 322 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 322) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 322)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)



# for /category/university-books/science-arts/bca link
# category id= 324
def university_sciencearts_bca(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 324 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 324) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 324)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)




# for /category/university-books/science-arts/bsc link
# category id= 325
def university_sciencearts_bsc(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 325 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 325) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 325)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	




# for /category/university-books/science-arts/ma link
# category id= 326
def university_sciencearts_ma(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 326 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 326) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 326)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	




# for /category/university-books/science-arts/mca link
# category id= 327
def university_sciencearts_mca(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 327 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 327) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 327)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)		




# for /category/university-books/science-arts/msc link
# category id= 328
def university_sciencearts_msc(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 328 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 328) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 328)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	




# for /category/university-books/science-arts/ba link
# category id= 323
def university_sciencearts_ba(request,pg):
	start= (int(pg)-1)*10
	cursor = connection.cursor()
	cursor.execute('''SELECT final.book_id, final.title, final.thumb, final.price, final.slug  from 
						(SELECT * FROM books WHERE category = 323 UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id = 323) UNION
						SELECT * FROM books WHERE category in (SELECT id from categories where parent_id in 
						(SELECT id from categories where parent_id = 323)))final ORDER BY is_out_of_stack, i_date DESC limit %s,10''', start)

	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]
	all_books= []
	for each_col in rows:
		each_book= {}
		for i in range(len(cols)):
			each_book[cols[i]]= each_col[i]
		all_books.append(each_book)	
	books_json= json.dumps(all_books)
	return HttpResponse(books_json)	



#---------------------------------------------------------------------------------------------	
#---------------------------------------------------------------------------------------------