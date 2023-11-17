from django.urls import path
from app import views
urlpatterns = [
    path('',views.index,name='index'),
    path('practice',views.practice,name='prac'),
    path('assignment',views.assignment,name='assgn'),
    path('tests',views.test,name='tests'),
    path('test1',views.test1,name='test1')
]
