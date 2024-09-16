# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.front_page, name='front_page'),
    path('insert/', views.dbactions, name='empinserturl'),
    path('select/', views.selectdata, name='empselecturl'),
    path('update/<int:eno>/', views.updatedata, name='empupdateurl'),
    path('delete/<int:eno>/', views.deletedata, name='empdeleteurl'),
]
