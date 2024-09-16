from django.db import models
from django.db.models.signals import pre_save,post_save
import time
from django.core.mail import send_mail
from django.conf import settings
# Create your models here.
class Department(models.Model):
    deptno = models.IntegerField(primary_key=True)
    deptname = models.CharField(max_length=20)

    def __str__(self) :
        return self.deptname
class Employee(models.Model):
    empno = models.IntegerField(primary_key=True)
    empname = models.CharField(max_length=20)
    salary = models.IntegerField()
    department = models.ForeignKey(Department,null=True, on_delete=models.CASCADE)
    image=models.ImageField(null=True,upload_to='media/images/')
    def __str__(self):
        return self.empname
        #return str(self.salary)
class Adhar(models.Model):
    aadhar_id = models.IntegerField(primary_key=True)
    issued_date = models.DateField(auto_now_add=True)
class Person(models.Model):
    pid=models.IntegerField(primary_key=True)
    pname=models.CharField(max_length=20)
    aadhar=models.OneToOneField(Adhar,null=True,on_delete=models.CASCADE)
# abstract class 
class Base1(models.Model):
    empno=models.IntegerField(primary_key=True)
    empname=models.CharField(max_length=20)
    class Meta:
        abstract = True

class Child1(Base1):
    phno=models.CharField(max_length=20)

class Child2(Base1):
    address=models.CharField(max_length=130)
#proxy inheritance
class Duplicate(Employee):
    class Meta:
        proxy=True
        ordering=['-salary']
#multitable inheritance
class Base2(models.Model):
    empno=models.CharField(primary_key=True,max_length=10)
    empname=models.CharField(max_length=20)
class Child3(Base2):
    address=models.CharField(max_length=100)
# many to many relation 
class Cars(models.Model):
    car_no=models.CharField(primary_key=True,max_length=20)
    car_model=models.CharField(max_length=20)
class Drivers(models.Model):
    license_no=models.CharField(max_length=20,primary_key=True)
    name=models.CharField(max_length=20)
    cars=models.ManyToManyField(Cars)

def pre_save_handler(sender,instance,**kwargs):
    print("pre_save_handler called")
    print(sender)
    print(instance)
    #time.sleep(30)
'''def post_save_handler(sender,instance,created,**kwargs):
   # print("post_save_handler called")
   # print(sender)
   # print(instance)
    #print(created)
    if created == True:
        sub  = 'test mail'
        to =['prudhvirajsuthapalli8@gmail.com']
        mesg =  dear sir/madam ,
        new employee has been created or inserted into employee table
        Employee details name ={} salary ={}.format(instance.empname, instance.salary)
        send_mail(subject=sub, message=mesg,from_email=settings.EMAIL_HOST_USER,recipient_list=to)
        
pre_save.connect(pre_save_handler, sender=Employee)
post_save.connect(post_save_handler, sender=Employee)'''