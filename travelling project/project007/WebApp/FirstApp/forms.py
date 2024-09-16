from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','username','password1','password2','email','is_superuser']