
from django.urls import path
from .import views
urlpatterns =[
   #path('',views.display),
   path('casestudy/',views.case_study),
   path('casestudy2/',views.case_study2, name='inserturl'),
   path('select/', views.selectdata, name='selecturl'),
   path('', views.loginpage,name='loginurl'),
   path('logout/', views.logoutpage,name='logouturl'),
   path('signup/', views.registeruser,name='signupurl'),
   path('home/', views.homepage,name='homeurl'),
   #path('insert/',views.insertform,name='inserturl'),
]