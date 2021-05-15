from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.http import HttpResponse
from account.forms import CustomerSignUpForm, ServiceProviderSignUpForm
from account.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

    
class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'register/customer.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('user')

class ServiceProviderSignUpView(CreateView):
    model = User
    form_class = ServiceProviderSignUpForm
    template_name = 'register/sp.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'ServiceProvider'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('adminlogins')