from django.urls import path
from . import views

urlpatterns=[
   
    path('add/',views.add,name='add'),
    path('den/',views.index,name='index'),
     path('signup', views.signup, name='index'),
     path('login', views.login, name='login'),
     path('dashboard', views.dashboard, name='dashboard'),
      path('logout',views.logout,name='home'),
       path('productList',views.productList,name='home'),
       path('newProduct',views.newProduct),
      path('',views.home,name='home'),
    
]