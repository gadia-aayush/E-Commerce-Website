from django.db import models

# Create your models here.
class Pincodes(models.Model):
    pincode = models.IntegerField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'pincodes'


class PinMap(models.Model):
    pincode = models.DecimalField(max_digits=38, decimal_places=0)
#    taluk = models.CharField(max_length=50, blank=True, null=True)
    districtname = models.CharField(max_length=50)
    statename = models.CharField(max_length=50)
    
    class Meta:
        managed = False
        db_table = 'pin_map'
