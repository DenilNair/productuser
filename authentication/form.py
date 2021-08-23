from django import forms
from .models import ProductList
 
class MyForm(forms.ModelForm):
  class Meta:
    model = ProductList
    fields = ["product_name", "product_desc","product_rate","product_quantity","product_Img"]
    labels = {'product_name': 'Name', 'product_desc': 'Description','product_rate':'rate','product_quantity':'Quantity','product_Img':'Image'}


    