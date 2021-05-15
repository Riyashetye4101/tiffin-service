from django.urls import path
from . import views


urlpatterns=[
    path('adminaccount/',views.adminentry,name='adminaccount'),
    path('menudrive/',views.menu,name='menu'),
    path('order/',views.order,name='order'),
    path('cd/<str:cust_id>',views.customerdetails,name='cd'),
    path('status/<str:order_id>',views.status,name='status'),
    path('delete/<int:pk_test>',views.delete,name='delete'),
    path('show_details/<str:cd_id>',views.details,name='show_details'),
    
    
    
]