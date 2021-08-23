from django.db import models

# Create your models here.
class ProductList(models.Model):
    product_name = models.CharField(max_length=100)
    product_desc = models.CharField(max_length=200)
    product_rate = models.IntegerField()
    product_quantity = models.IntegerField()
    product_Img = models.ImageField(upload_to='images/')
    product_user=models.CharField(max_length=50)

    def _isvalid(product_name,product_desc,product_rate,product_quantity,product_Img,product_user):
        if product_name:
            if product_desc:
                if product_rate:
                    if product_quantity:
                        if product_Img:
                            if product_user:
                                return True

                            

    
        else:
            return False                          
