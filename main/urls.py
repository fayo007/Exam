from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('service',views.service, name='service'),
    path('blog',views.blog, name='blog'),
    path('create_contact',views.create_contact, name='create_contact'),
    path('staff_img',views.staff_img,name='staff_img')
]
