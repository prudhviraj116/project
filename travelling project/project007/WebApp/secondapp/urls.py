from django.urls import path
from . import views

urlpatterns =[
    path('',views.processing),
    path('greet/',views.greetings)
]