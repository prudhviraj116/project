from django.contrib import admin
from .models import Employee
from .models import Department

admin.site.register(Department)
# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display = ('empno', 'empname', 'salary','grade')


