from django import forms
from .models import Category, Product


class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ("Name", "Description")


class ProductForm(forms.ModelForm):
	class Meta:
		model=Product
		fields=("Categories", "Name","Image","IDorSNO","Description","Price","NumbersAvailable")
		
