from django.contrib import admin
from .models import Employee,Department,Adhar,Person,Child1,Child2,Duplicate,Person

# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display = ('empno', 'empname', 'salary','grade')
    list_editable = ('empname', 'salary')
    list_filter = ('salary', 'empname')
    def grade(self,obj):
        if obj.salary>200000:
            return 'high'
        else:
            return 'low'
admin.site.register(Employee,EmpAdmin)
admin.site.register(Department)
admin.site.register(Adhar)
admin.site.register(Person)
admin.site.register(Child1)
admin.site.register(Child2)
admin.site.register(Duplicate,EmpAdmin)