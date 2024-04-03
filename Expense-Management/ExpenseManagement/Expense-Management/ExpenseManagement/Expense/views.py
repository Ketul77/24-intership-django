from django.shortcuts import render
from django.views.generic.edit import CreateView 
from .forms import ExpenseCreationForm
from django.views.generic import ListView ,DetailView 
from django.views.generic.edit import UpdateView , DeleteView
from .models import Expense 
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import View
from django.views import View
from django.shortcuts import redirect,get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.views.decorators.http import require_POST


# Create your views here.
class ExpenseCreationView(CreateView):
    template_name = 'Expense/create.html'
    model= Expense
    form_class = ExpenseCreationForm
    success_url = '/Expense/list'

    def form_valid(self, form):
        form.instance.user = self.request.user  # Assigning the logged-in user to the 'user' field
        return super().form_valid(form)
    
   
class Expenselistview(ListView):
    template_name = 'Expense/list.html'
    model = Expense
    context_object_name = "Expense"


# @method_decorator(login_required, name='dispatch')
    
class ExpenseDetailview(DetailView):
    model = Expense
    template_name='Expense/Expense_detail.html'
    context_object_name ="Expense"

   
    
class ExpenseUpdateview(UpdateView):
    model = Expense
    fields = "__all__"
    success_url= '/Expense/list'
    template_name ='Expense/Edit.html'


class ExpenseDeleteview(DeleteView):
    model = Expense
    template_name = 'Expense/Delete.html'
    success_url = reverse_lazy('list')

    


def pieChart(request):
    labels =[]
    data =[]
    
    queryset = Expense.objects.order_by('-amount')[:5]
    print(queryset)


    for exp in queryset:
        print(exp)
        print(exp.amount)
        labels.append(exp.category.name)
        data.append(float(exp.amount))
        print(data)
        print(labels)
        #data.append(exp.amount)
        
    return render(request, 'Expense/pie_chart.html',{
        'labels':labels,
        'data':data
    })        


class receiptListView(ListView):
    template_name = 'Expense/receipt_list.html'
    model = Expense
    context_object_name = 'Expense' 
     
@method_decorator(require_POST, name='dispatch')

class updatestatusview(View):

    def post(self,request,pk):
        print("pk..",pk)

        expense = get_object_or_404(Expense, id=pk)
        print("expense..", expense)
        print("Current status:", expense.status)
        if expense.status == "uncleared":
            expense.status = "void"
        elif expense.status == "void":
            expense.status = "done"
        print("New status:", expense.status)

        expense.save()
        return redirect(reverse("list"))


        