from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import products
from django.contrib.auth import authenticate,login,logout
from . forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required,user_passes_test
from .decorator import checkSuperUser
# Create your views here.
def display(request):
    return HttpResponse('hello world,we are learning Django')
def case_study(request):
    if request.method == 'POST':
        input_text = request.POST.get('t1', '')
        words = input_text.split()
        count = len(words)
        even=count % 2 == 0
        return render(request, 'casestudy.html', {'word_counts': words, 'count': count, 'even': even})
    return render(request, 'casestudy.html')
#@user_passes_test(lambda user: user.is_superuser)
@checkSuperUser
def case_study2(request):
    data=products.objects.all()
    if request.method == 'POST':
        items=request.POST.get('items')
        price=request.POST.get('price')
        quantity=request.POST.get('quantity')
        total=request.POST.get('total')
        products.objects.create(items=items, price=price, quantity=quantity, total=total)
        return redirect('selecturl')
    return render(request,'insert.html',{'data':data})
@login_required(login_url='loginurl')
def selectdata(request):
    data = products.objects.all()
    return render(request, 'select.html', {'data': data})
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
    return render(request,'login.html')
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
    return render(request,'home.html')