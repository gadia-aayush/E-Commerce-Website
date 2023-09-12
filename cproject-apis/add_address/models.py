from django.db import models


class Useraddresses(models.Model):
    user_id = models.IntegerField()
    title = models.CharField(max_length=225, blank=True, null=True)
    rec_name = models.CharField(max_length=225, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    address = models.TextField()
    landmark = models.CharField(max_length=225)
    phone_no = models.CharField(max_length=50, blank=True, null=True)
    state_name = models.CharField(max_length=200, blank=True, null=True)
    city_name = models.CharField(max_length=225)
    country_name = models.CharField(max_length=100)
    address_type = models.IntegerField()
    is_primary = models.CharField(max_length=1)

    class Meta:
        managed = True
        db_table = 'useraddresses'