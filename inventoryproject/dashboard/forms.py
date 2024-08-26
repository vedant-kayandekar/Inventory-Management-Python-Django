from django import forms  
from .models import Product, Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','category','quantity']
        
class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','category','quantity']
        # success_url = 'dashboard-product'

class OrderAdd(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'order_quantity']