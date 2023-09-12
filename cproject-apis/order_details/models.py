from django.db import models

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_no = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField()
    amount = models.FloatField()
    no_of_book = models.IntegerField()
    status = models.CharField(max_length=255, blank=True, null=True)
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
        managed = True
        db_table = 'orders'


class OrderAddress(models.Model):
    order_id = models.IntegerField()
    rec_name = models.CharField(max_length=255)
    email = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.IntegerField()
    address = models.TextField()
    landmark = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    courier_name = models.CharField(max_length=255, blank=True, null=True)
    awb = models.CharField(max_length=255, blank=True, null=True)
    i_date = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'order_address'


class Useraddresses(models.Model):
    address_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    title = models.CharField(max_length=225, blank=True, null=True)
    rec_name = models.CharField(max_length=225, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    address = models.TextField()
    landmark = models.CharField(max_length=225)
    phone_no = models.CharField(max_length=50, blank=True, null=True)
    address_type = models.IntegerField()
    is_primary = models.CharField(max_length=1)
    state_name = models.CharField(max_length=200, blank=True, null=True)
    city_name = models.CharField(max_length=225)
    country_name = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'useraddresses'        

