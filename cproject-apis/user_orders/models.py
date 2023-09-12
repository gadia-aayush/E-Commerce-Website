from django.db import models


class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    sku = models.CharField(max_length=225)
    isbn = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, blank=True, null=True)
    thumb = models.CharField(max_length=225)
    author = models.CharField(max_length=255, blank=True, null=True)
    publication = models.CharField(max_length=225, blank=True, null=True)
    category = models.IntegerField()
    publication_date = models.IntegerField(blank=True, null=True)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    weight = models.CharField(max_length=225, blank=True, null=True)
    binding = models.CharField(max_length=225, blank=True, null=True)
    edition = models.CharField(max_length=225, blank=True, null=True)
    shipping_cost = models.FloatField()
    book_desc = models.TextField(blank=True, null=True)
    book_desc_url = models.CharField(max_length=255, blank=True, null=True)
    no_of_pages = models.CharField(max_length=225, blank=True, null=True)
    language = models.CharField(max_length=225, blank=True, null=True)
    is_allow_multi_order = models.CharField(max_length=1)
    qty = models.IntegerField()
    published = models.CharField(max_length=1)
    is_cashondelivery = models.CharField(max_length=1)
    is_featured = models.CharField(max_length=1)
    is_publication_house = models.CharField(max_length=1)
    is_out_of_stack = models.CharField(max_length=1)
    is_deleted = models.CharField(max_length=1)
    is_doubtful = models.CharField(max_length=1)
    keywords = models.TextField(blank=True, null=True)
    i_by = models.IntegerField()
    i_date = models.IntegerField()
    u_by = models.IntegerField()
    u_date = models.IntegerField()
    uploaded_by = models.CharField(max_length=255, blank=True, null=True)
    actual_date_upload = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'books'


class OrderBooks(models.Model):
    order_book_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    book_id = models.IntegerField()
    book_inv_id = models.CharField(max_length=225)
    qty = models.IntegerField()
    racks = models.CharField(max_length=225)
    handling_charge = models.CharField(max_length=255)
    is_thanks_mail_sent = models.CharField(max_length=1)
    is_book_found = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'order_books'


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_no = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField()
    amount = models.FloatField()
    no_of_book = models.IntegerField()
    status = models.IntegerField()
    payusing = models.CharField(max_length=225)
    biiling_add_id = models.IntegerField()
    shipping_add_id = models.IntegerField()
    i_by = models.IntegerField()
    i_date = models.IntegerField()
    u_by = models.IntegerField()
    u_date = models.IntegerField()
    is_thanks_mail_sent = models.CharField(max_length=1)
    is_notification_sent = models.CharField(max_length=1)
    fast_delivery = models.IntegerField()
    shipping_handling_donation = models.FloatField(blank=True, null=True)
    prepaid_discount = models.IntegerField(blank=True, null=True)
    delivery_charge_newbooks = models.IntegerField(blank=True, null=True)
    cod_charge = models.FloatField(blank=True, null=True)
    user_rating = models.IntegerField(blank=True, null=True)
    coupon_id = models.CharField(max_length=255, blank=True, null=True)
    coupon_amount = models.FloatField(blank=True, null=True)
    cod_offer_interested = models.IntegerField()
    actual_date_upload = models.CharField(max_length=255, blank=True, null=True)
    wallet_used = models.FloatField(blank=True, null=True)
    courier_name = models.TextField(blank=True, null=True)
    weight = models.CharField(max_length=255, blank=True, null=True)
    expected_price = models.CharField(max_length=255, blank=True, null=True)
    shipment_tracking_no = models.CharField(max_length=100, blank=True, null=True)
    payment_url = models.CharField(max_length=255, blank=True, null=True)
    payment_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'
