from django.urls import path
from . import views

urlpatterns = [
    #path('', views.firstform),
    path('', views.loginpage,name='loginurl'),
    path('logout/', views.logoutpage,name='logouturl'),
    path('signup/', views.registeruser,name='signupurl'),
    path('home/', views.homepage,name='homeurl'),
    path('insert/',views.insertform,name='inserturl'),
    path('select/<int:pno>',views.selectform,name='selecturl'),
    path('details/<int:eno>',views.detailsform,name='empdetailurl'),
]