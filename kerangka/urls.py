from unicodedata import name
from django.urls import path
from .import views

urlpatterns = [
    # path('',views.awal,name='awal'),
    path('',views.Home,name='home'),
    path('Produk',views.Produk,name='produk'),
    path('Registrasi',views.Registrasi,name='registrasi'),
    path('Logout', views.logout, name='logout'),
    path('Login',views.Login,name='login'),
    path('Scheduler',views.Scheduler,name='scheduler'),
    path('Listjobrunning',views.Listjobrunning,name='listjobrunning')
    #path('InsertRegistrasi',views.InsertRegistrasi,name='Insertregistrasi'),
    #path('InsertRegistrasi',views.InsertRegistrasi , name='insert_data')

    
]
