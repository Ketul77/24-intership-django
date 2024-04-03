from django.db import models
from user.models import User



PAYMENT_METHOD_CHOICES = [
    ("cash", "Cash"),
    ("cheque", "Cheque"),
    ("creditCard", "Credit Card")
]

STATUS_CHOICES = [
    ("cleared", "Cleared"),
    ("uncleared", "Uncleared"),
    ("void", "Void")
]

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "category"

    def __str__(self):
        return self.name    

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
      
    class Meta:
        db_table = "subcategory"

    def __str__(self):
        return self.name  

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    paymentmethod = models.CharField(max_length=100, choices=PAYMENT_METHOD_CHOICES)
    expdate = models.DateField()
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    description = models.TextField()
    receipt = models.ImageField(upload_to="uploads/",null=True)

    class Meta:
        db_table = "Expense"


   