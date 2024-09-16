from django.urls import path
from . import views

urlpatterns =[
    path('first/',views.FirstClass.as_view()),
    path('second/',views.SecondClass.as_view()),
    path('select/',views.SelectView.as_view(),name='classselecturl'),
    path('create/',views.InsertView.as_view()),
    path('update/<int:pk>',views.Modifyview.as_view()),
    path('delete/<int:pk>',views.Removeview.as_view()),
]