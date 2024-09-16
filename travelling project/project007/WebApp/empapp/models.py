# models.py

from django.db import models
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
    
    def __str__(self):
        return self.empname