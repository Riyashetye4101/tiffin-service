from django.urls import path
from . import views
 
urlpatterns=[
    
    path('',views.userlogin,name='user'),
    path('adminlogin',views.adminlogin,name='adminlogins'),
    path('userlogin',views.userlogin,name='user'),
    path('logout_user',views.logout_user,name='logout_user')
  
    
]

