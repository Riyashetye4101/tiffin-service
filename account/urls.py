from django.urls import path
from . import views
urlpatterns = [
    
    path('Customer',views.CustomerSignUpView.as_view(),name='CustomerSignUpView'),
    path('serviceprovider',views.ServiceProviderSignUpView.as_view(),name='ServiceProviderSignUpView'),
    
]