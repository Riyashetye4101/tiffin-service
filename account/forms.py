from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from account.models import Customer, User, ServiceProvider


class CustomerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    alt_phone_number = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.first_name=self.cleaned_data.get('first_name')
        user.last_name=self.cleaned_data.get('last_name')
        user.email=self.cleaned_data.get('email')
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user)
        customer.phone_number = self.cleaned_data.get('phone_number')
        customer.alt_phone_number=self.cleaned_data.get('alt_phone_number')
        # student.interests.add(*self.cleaned_data.get('interests'))
        customer.save()
        return user

class ServiceProviderSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    admin_name = forms.CharField(required=True)
    company_name = forms.CharField(required=True)
    phone_no = forms.CharField(required=True)
    alt_phone_no = forms.CharField(required=True)
    state = forms.CharField(required=True)
    city = forms.CharField(required=True)
    pin_no = forms.CharField(required=True)
    Area_name = forms.CharField(required=True)
    land_mark = forms.CharField(required=True)
    building_name = forms.CharField(required=True)
    flate_number = forms.CharField(required=True)
    time = forms.TimeField(required=True)
    to = forms.TimeField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_sp = True
        user.save()
        sp = ServiceProvider.objects.create(user=user)
        sp.admin_name =self.cleaned_data.get('admin_name')
        sp.company_name =self.cleaned_data.get('company_name')
        sp.phone_no = self.cleaned_data.get('phone_no')
        sp.alt_phone_no =self.cleaned_data.get('alt_phone_no')
        sp.state = self.cleaned_data.get('state')
        sp.city = self.cleaned_data.get('city')
        sp.pin_no = self.cleaned_data.get('pin_no')
        sp.Area_name = self.cleaned_data.get('Area_name')
        sp.land_mark = self.cleaned_data.get('land_mark')
        sp.building_name =self.cleaned_data.get('building_name')
        sp.flate_number = self.cleaned_data.get('flate_number')    
        sp.time = self.cleaned_data.get('time')
        sp.to = self.cleaned_data.get('to')
        sp.save()
        return user