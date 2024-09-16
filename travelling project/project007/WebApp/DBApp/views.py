from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Employee,Department
# Create your views here.
def dbactions(request):
    depts= Department.objects.all()
    if request.method =='POST':
        eno = request.POST.get('eno')
        ename = request.POST.get('ename')
        esal = request.POST.get('esal')
        dno= request.POST.get('deptno')
        #emp=Employee(empno=eno,empname=ename, salary=esal)
        #emp.save()
        dept=Department.objects.get(deptno=dno)
        Employee.objects.create(empno=eno,empname=ename, salary=esal,department=dept)
        return redirect('empselecturl')
    return render(request,'dbapp/insert.html',{'depts':depts})

def selectdata(request):
    employees = Employee.objects.all()  
    return render(request, 'dbapp/selectdata.html', {'employees': employees})
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
    
    return render(request, 'dbapp/updatedata.html', {'employee': empObj, 'depts': depts})

def deletedata(request,eno):
    emp = Employee.objects.get(empno=eno)
    if request.method == 'POST':
        emp.delete()
        return redirect('empselecturl')
    return render(request, 'dbapp/delete.html',{'employee':emp})