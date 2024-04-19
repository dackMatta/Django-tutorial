from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('base/',views.base, name='base'),

]