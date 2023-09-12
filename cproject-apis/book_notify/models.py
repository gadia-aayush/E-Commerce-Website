from django.db import models


class Booknotify(models.Model):
    bookid = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()
    user_email = models.CharField(max_length=100, blank=True, null=True)
    book_name = models.CharField(max_length=255, blank=True, null=True)
    isbn = models.CharField(max_length=255, blank=True, null=True)
    is_mail_sent = models.CharField(max_length=10)

    class Meta:
        managed = True
        db_table = 'booknotify'


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
    handling_cost = models.FloatField(blank=True, null=True)
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
        managed = True
        db_table = 'books'

        