from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from DBApp.models import Employee
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class FirstClass(View):
    def get(self,request):
        return render(request,'ClassApp/class.html')
    def post(self,request):
        data=request.POST['t1']
        return render(request,'ClassApp/class.html',{'data':data})
    
class SecondClass(FirstClass):
    def post(self, request):
        data=request.POST['t1']*3
        return render(request,'ClassApp/class.html',{'data':data})
class SelectView(ListView):
    model = Employee
    template_name = 'ClassApp/employee_select.html'
class InsertView(CreateView):
    model = Employee
    fields = '__all__'
    template_name = 'ClassApp/employee_insert.html'

    def get_success_url(self):
        return reverse('classselecturl')
class Modifyview(UpdateView):
    model = Employee
    fields = '__all__'
    template_name= 'ClassApp/employee_update.html'
    def get_success_url(self):
        return reverse('classselecturl')
class Removeview(LoginRequiredMixin,DeleteView):
    login_url = 'loginurl'
    model = Employee
    fields = '__all__'
    template_name= 'ClassApp/employee_delete.html'
    def get_success_url(self):
        return reverse('classselecturl')