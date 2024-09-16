from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from . forms import FirstForm,Empform,RegisterForm
from DBApp.models import Employee
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.forms import UserCreationForm
from .decorator import checkSuperUser,checkUser
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page
# Create your views here.
def firstform(request):
    empty_form = FirstForm()
    if request.method == 'POST':
        dataForm=FirstForm(request.POST)
        if dataForm.is_valid()==True:
            v1=dataForm.cleaned_data['value1']
            v2=dataForm.cleaned_data['value2']
            return HttpResponse('addition is'+str(v1+v2))
        else:
            print(dataForm.errors)
            return HttpResponse(str(dataForm.errors))
    return render(request, 'formapp/first.html', {'form': empty_form})
#@user_passes_test(lambda user: user.is_superuser)
#@checkSuperUser
@checkUser(allowed_groups=['python'])
def insertform(request):
    empty_form =Empform()
    print(request.x)
    if request.method == 'POST':
        dataForm=Empform(request.POST,request.FILES)
        if dataForm.is_valid()==True:
           dataForm.save()
           messages.success(request, 'Record inserted successfully')
           return render(request,'formapp/insert.html',{'form':empty_form})
        else:
            messages.error(request, 'Record not inserted successfully')
            return render(request,'formapp/insert.html',{'form':dataForm})
    #else:
        #print(dataForm.errors)
        #return HttpResponse(str(dataForm.errors))
    return render(request, 'formapp/insert.html', {'form': empty_form})
@cache_page(60*3)
@login_required(login_url='loginurl')
def selectform(request,pno):
    print(request.x)
    emps=Employee.objects.all()
    paginator_obj = Paginator(emps, 4)
    page=paginator_obj.get_page(pno)
    return render(request, 'formapp/select.html', {'employees': page})
def detailsform(request,eno):
   emp= Employee.objects.get(empno=eno)
   return render(request, 'formapp/details.html', {'employee':emp})
def loginpage(request):
    if request.method=='POST':
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        userobj=authenticate(username=uname,password=pwd)
        if userobj==None:
            return redirect('loginurl')
        else:
            login(request,user=userobj)
            return redirect('homeurl')
    return render(request,'formapp/login.html')

def logoutpage(request):
    logout(request)
    return redirect('loginurl')
def registeruser(request):
    emptyobj = RegisterForm()
    if request.method=='POST':
        userForm=RegisterForm(request.POST)
        if userForm.is_valid():
            userForm.save()
            return redirect('loginurl')
        else:
            return render(request,'formapp/register.html',{'form':userForm})
    return render(request,'formapp/register.html',{'form':emptyobj})
def homepage(request):
    return render(request,'formapp/home.html')