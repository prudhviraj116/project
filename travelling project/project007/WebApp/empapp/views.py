# views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee,Department

def front_page(request):
     employees = Employee.objects.all()
     return render(request, 'empapp/front_page.html', {'employees': employees})

def dbactions(request):
    depts= Department.objects.all()
    if request.method == 'POST':
        eno = request.POST.get('eno')
        ename = request.POST.get('ename')
        esal = request.POST.get('esal')
        dno = request.POST.get('deptno')
        dept=Department.objects.get(deptno=dno)
        Employee.objects.create(empno=eno, empname=ename, salary=esal,department=dept)
        print(request.POST)
        return redirect('empselecturl')
    return render(request, 'empapp/insert.html',{'depts':depts})


def selectdata(request):
    employees = Employee.objects.all()
    return render(request, 'empapp/selectdata.html', {'employees': employees})

def updatedata(request, eno):
    empObj = Employee.objects.get(empno=eno)
    depts = Department.objects.all()
    if request.method == 'POST':
        eno = request.POST.get('eno')
        ename = request.POST.get('ename')
        esal = request.POST.get('esal')
        dno = request.POST.get('deptno')
        dept = Department.objects.get(deptno=dno)
        empObj.empno = eno
        empObj.empname = ename
        empObj.salary = esal
        empObj.department = dept
        empObj.save()
        
        return redirect('empselecturl')
    
    return render(request, 'empapp/updatedata.html', {'employee': empObj, 'depts': depts})
def deletedata(request, eno):
    emp = Employee.objects.get(empno=eno)
    if request.method == 'POST':
        emp.delete()
        return redirect('empselecturl')
    return render(request, 'empapp/delete.html', {'employee': emp})
