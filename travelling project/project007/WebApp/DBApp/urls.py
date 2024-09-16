from django.urls import path
from . import views
urlpatterns =[
    path('insert/',views.dbactions,name='empinserturl'),
    path('select/', views.selectdata,name='empselecturl'),
    path('update/<int:eno>', views.updatedata,name='empupdateurl'),
    path('delete/<int:eno>', views.deletedata,name='empdeleteurl'),

 ]