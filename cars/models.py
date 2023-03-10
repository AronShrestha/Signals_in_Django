from django.db import models
from buyers.models import Buyer
import uuid
# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveBigIntegerField()
    buyer = models.ForeignKey(Buyer,on_delete=models.CASCADE)
    code = models.CharField(max_length=10,blank=True)

    def __str__(self) -> str:
        return f"{self.name} -{self.price} -{self.buyer}"
    
    # def save(self,*args,**kwargs):
    #     """Overriding the 'save' method"""
    #     print(args)
    #     print("Args",*args)
    #     print("kwargs",**kwargs)
    #     if self.code == "":
    #         self.code = str(uuid.uuid4()).replace("-","").upper()[:10]
    #     return super().save(*args,**kwargs)
