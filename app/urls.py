from django.urls import path
from app import views
urlpatterns = [
    path('',views.index,name='index'),
    path('practice',views.practice,name='prac'),
    path('assignment',views.assignment,name='assgn')
]
