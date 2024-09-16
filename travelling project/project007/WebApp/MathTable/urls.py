from django.urls import path
from. import views

urlpatterns =[
    path('',views.generateTable),
    path('calculator/',views.calculator)
]