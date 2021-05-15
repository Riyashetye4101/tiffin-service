from django.urls import path
from . import views
 
urlpatterns=[
    path('home',views.home,name='home'),
    path('add_sp/<str:pk_test>',views.add_sp,name='add_sp'),
    path('details/<str:id_test>',views.detail,name='details'),
    path('your_account',views.account,name='your_account'),
    path('remove/<str:id1>',views.remove,name='remove'),
    path('delete/<str:reset_id>/<str:pl>',views.delete,name='delete'),
    path('user_order',views.order,name='user_order'),
    path('cancel/<str:order_id>',views.cancel,name='cancel'),
    path('select/<str:sp_id>',views.select,name='select'),
    path('duration/<str:data>/<str:company_id>',views.duration,name='duration'),
    path('address/<str:or_id>',views.order_address,name='address'),
    path('visite/<str:id_order>',views.update_menu,name='visite'), 
    path('add_item/<str:item_id>/<str:order_id>',views.add_item,name='add_item'),
    path('tiffin/<str:pk_order>',views.tiffin,name='tiffin'),
]
