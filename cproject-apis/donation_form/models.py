from django.db import models


class Donationreqs(models.Model):
    user_id = models.IntegerField()
    volunteer_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    mobile = models.CharField(db_column='Mobile', max_length=100, blank=True, null=True)  # Field name made lowercase.
    address = models.TextField()
    landmark = models.CharField(db_column='Landmark', max_length=225, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=225)
    zipcode = models.IntegerField()
    no_of_book = models.IntegerField()
    no_of_cartons = models.IntegerField()
    app_books_weight = models.IntegerField()
    donated_book_category = models.CharField(max_length=255)
    how_do_u_know_abt_us = models.CharField(max_length=225)
    wastage = models.IntegerField()
    document_mail_sent = models.CharField(max_length=1)
    is_blocked = models.CharField(max_length=1)
    i_date = models.IntegerField()
    u_date = models.IntegerField(blank=True, null=True)
    is_paid_donation = models.CharField(max_length=1)
    donor_name = models.CharField(max_length=45, blank=True, null=True)
    pickup_date_time = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'donationreqs'
