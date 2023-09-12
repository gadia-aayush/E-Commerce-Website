from django.db import models

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    amount = models.FloatField()
    payusing = models.CharField(max_length=225)    

    class Meta:
        managed = False
        db_table = 'orders'


class OrderAddress(models.Model):
    order_id = models.IntegerField()
    pincode = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_address'