#from rest_framework.serializers import ModelSerializer,ValidationError
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from DBApp.models import Employee
from django.contrib.auth.models import User
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        #fields = ['empno','empname','salary']
        fields= '__all__'
    def validate(self,data):
        if data['salary']<0:
            raise serializers.ValidationError({'error':'salary should be greater than 0'})
        else:
            return data
'''class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username', 'password', 'email']'''
class UserSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=100)
    email=serializers.EmailField()
    password1=serializers.CharField(max_length=100)
    password2=serializers.CharField(max_length=100)

    def validate(self, data):
        if data['password1']!=data['password2']:
            raise serializers.ValidationError({'error':'password does not match'})
        else:
            return data
    def createuser(self, user_data):
        uobject=User.objects.create(username=user_data['username'], email=user_data['email'])
        uobject.set_password(user_data['password1'])
        uobject.save()

        Token.objects.create(user=uobject)