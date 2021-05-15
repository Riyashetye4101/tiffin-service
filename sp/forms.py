from django import forms
from django.forms import ModelForm
from account.models import Menu

#create a venue form
class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = ('item_name','price','category')
        # widgets = {
        # 'name':forms.TextInput(attrs={'class':'form-control'}),
        # 'address':forms.TextInput(attrs={'class':'form-control'}),
        # 'mobileno':forms.TextInput(attrs={'class':'form-control'}),
        # 'zip_code':forms.TextInput(attrs={'class':'form-control'}),
        # 'web':forms.TextInput(attrs={'class':'form-control'}),
        # 'email_address':forms.EmailInput(attrs={'class':'form-control'})
        # }
        # 