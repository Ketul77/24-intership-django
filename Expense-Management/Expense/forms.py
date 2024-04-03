from django import forms
from .models import Expense , Category ,Subcategory


class ExpenseCreationForm(forms.ModelForm):
    class Meta:
        model = Expense
        # fields ='__all__'
        exclude = ['user']
        widgets = { 
              'expdate' :forms.DateInput(attrs={'type':'date'})
              }


class categoryForm(forms.ModelForm):
    class meta:
         model = Category
         fields = '__all__'

class SubcategoryForm(forms.ModelForm):
    class meta:
        model = Subcategory
        fields = '__all__'    


