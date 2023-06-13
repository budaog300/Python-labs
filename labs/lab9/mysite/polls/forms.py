from django import forms
from .models import Item, Cashier, Store, Check, Sale
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        labels = {
            'name': 'ФИО пациента',
        }


class CashierForm(forms.ModelForm):
    class Meta:
        model = Cashier
        fields = ['name', 'phone_number']
        labels = {
            'name': 'ФИО врача',
            'phone_number': 'Номер телефона врача',
        }


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'address']
        labels = {
            'name': 'Название поликлиники',
            'address': 'Адрес поликлиники',
        }



class CheckForm(forms.ModelForm):
    class Meta:
        model = Check
        fields = ['cashier', 'store', 'date_time', 'total_sum']
        labels = {          
            'cashier': 'Врач',            
            'store': 'Поликлиника',
            'date_time': 'Дата обращения',
            'total_sum': 'Причина обращения', 
        }
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),          
        }      


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['check_id', 'item', 'quantity']
        labels = {
            'check_id': 'Номер обращения',
            'item': 'ФИО пациента',
            'quantity': 'Длительность',
        }

        
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']