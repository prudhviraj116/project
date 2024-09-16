from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authentication import TokenAuthentication
from DBApp.models import Employee
from .serializers import EmployeeSerializer,UserSerializer
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST,HTTP_201_CREATED
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListCreateAPIView
import json
# Create your views here.
def display(obj):
    print('some data is processing')
    return obj.data['empno'],obj.data['empname'],obj.data['salary'],obj.data['image']
def employeeapi(request):
    #data={'empno':1,'empname':'raju','salary':10000}
    data=Employee.objects.all()
    emp=[{'empno':rec.empno,'empname':rec.empname} for rec in data]
    #output=json.dumps(data)
    output=json.dumps(emp)
    return JsonResponse(output,safe=False)
'''@api_view(['GET'])
def employeerestapi(request):
    empData= Employee.objects.all()
    empDetails = EmployeeSerializer(empData,many=True)
    return Response(data=empDetails.data)'''

#@authentication_classes([TokenAuthentication])
@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
#@permission_classes([IsAdminUser])
def empgetapi(request):
    if request.method=='POST':
        empobj=EmployeeSerializer(data=request.data)
        if empobj.is_valid():
            empobj.save()
            display(empobj)
            return Response(status=HTTP_201_CREATED)
        else:
            return Response(empobj.errors,status=HTTP_400_BAD_REQUEST)
    empData= Employee.objects.all()
    empobj = EmployeeSerializer(empData,many=True)
    return Response(empobj.data,status=HTTP_200_OK)
    #return Response(empobj.data,status=HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def updateempapi(request,pk):
    empobj= Employee.objects.get(empno=pk)
    if request.method=='PUT':
        seriaobj=EmployeeSerializer(empobj,data=request.data)
        if seriaobj.is_valid():
            seriaobj.save()
            return Response(status=HTTP_200_OK)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        empobj.delete()
        return Response(status=HTTP_200_OK)
    if request.method == 'GET':
        seriaobj=EmployeeSerializer(empobj)
        return Response(seriaobj.data,status=HTTP_200_OK)
@api_view(['POST'])
def registeruserapi(request):
    userobj=UserSerializer(data=request.data)
    if userobj.is_valid():
        #userobj.save()
        userobj.createuser(userobj.data)
        return Response(status=HTTP_201_CREATED)
    else:
        return Response(userobj.errors,status=HTTP_400_BAD_REQUEST)

class EmpClassAPI(APIView,PageNumberPagination):
    #authentication_classes([TokenAuthentication])
    #permission_classes([IsAuthenticated])
    def get(self,request):
        emps= Employee.objects.all()
        page=self.paginate_queryset(emps,request)
        if page is not None:
            empserialize=EmployeeSerializer(page,many=True)
            return self.get_paginated_response(empserialize.data)
        empdata = EmployeeSerializer(emps,many=True)
        return Response(empdata.data,status=HTTP_200_OK)
    def post(self,request):
        empobj=EmployeeSerializer(data=request.data)
        if empobj.is_valid():
            empobj.save()
            display(empobj)
            return Response(status=HTTP_201_CREATED)
        else:
            return Response(empobj.errors,status=HTTP_400_BAD_REQUEST)

class EmpGenricAPI(ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    pagination_classes=PageNumberPagination


class EmpModifyAPI(APIView):
    #authentication_classes=[TokenAuthentication]
    #permission_classes=[IsAuthenticated]
    def put(self,request,pk):
        existed_emp=Employee.objects.get(empno=pk)
        empobj=EmployeeSerializer(existed_emp,data=request.data)
        if empobj.is_valid():
            empobj.save()
            return Response(status=HTTP_200_OK)
        else:
            return Response(empobj.errors,status=HTTP_400_BAD_REQUEST)
    def get(self,request,pk):
        existing_emp=Employee.objects.get(empno=pk)
        empobj=EmployeeSerializer(existing_emp)
        return Response(empobj.data,status=HTTP_200_OK)