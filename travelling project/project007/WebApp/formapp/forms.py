from typing import Any
from django import forms
from DBApp .models import Employee
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
def validatevalue(val):
    if val<100:
        raise  forms.ValidationError('should be less than 100')
  
class FirstForm(forms.Form):
    value1=forms.IntegerField()
    value2=forms.IntegerField(validators=[validatevalue])
    doj=forms.DateField(widget=forms.SelectDateWidget)
    def clean_value1(self):
        v1=self.cleaned_data['value1']
        if v1<0:
            raise  forms.ValidationError('negative value are not allowed')
        return v1
    ''' def clean_value2(self):
        v2=self.cleaned_data['value2']
        if v2<100:
            raise  forms.ValidationError('should not be less than 100')
        return v2'''
class Empform(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','username','password1','password2','email','is_superuser']