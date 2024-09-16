from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns =[
    path('registeruser/',views.registeruserapi),
    path('login/',obtain_auth_token),
    path('getemployeedata/',views.employeeapi),
    #path('getemprestapi/',views.employeerestapi),
    path('getemprestapi/',views.empgetapi),
    path('modify/<int:pk>/',views.updateempapi),
    path('getempclassapi/',views.EmpClassAPI.as_view()),
    path('getempgenericapi/',views.EmpGenricAPI.as_view()),
    path('classmodify/<int:pk>/',views.EmpModifyAPI.as_view()),
]