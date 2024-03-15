from django.contrib import admin
from django.urls import path,include
from .views import ExpenseCreationView , Expenselistview , ExpenseDetailview , ExpenseUpdateview ,ExpenseDeleteview ,receiptListView,pieChart,updatestatusview
from .import views

urlpatterns = [

    path("create/",ExpenseCreationView.as_view(),name="create"),
    path("list/",Expenselistview.as_view(),name ="list"),
    path('Expense_detail/<int:pk>/',ExpenseDetailview.as_view(), name='Expense_detail'),
    path('Edit/<int:pk>/', ExpenseUpdateview.as_view(), name='Edit'),
    path("Delete/<int:pk>/",ExpenseDeleteview.as_view(),name='Delete'),
    path("chart/",views.pieChart,name="chart"),
    path("receipt_list/",receiptListView.as_view() , name="receipt_list"),
    path("update_status/<int:pk>/update_status/",views.updatestatusview.as_view(),name="update_status")
    
]
