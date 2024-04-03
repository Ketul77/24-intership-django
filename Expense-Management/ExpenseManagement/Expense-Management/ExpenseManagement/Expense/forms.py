from django import forms
from .models import Expense , Category ,Subcategory


class ExpenseCreationForm(forms.ModelForm):
    class Meta:
        model = Expense
        # fields ='__all__'
        exclude = ['user']


class categoryForm(forms.ModelForm):
    class meta:
         model = Category
         fields = '__all__'

class SubcategoryForm(forms.ModelForm):
    class meta:
        model = Subcategory
        fields = '__all__'    


