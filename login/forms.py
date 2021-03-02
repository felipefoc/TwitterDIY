from django import forms
#from account.models import Account

#class LoginForm(forms.ModelForm):

YEARS= [x for x in range(1901,2022)]

class UserForm(forms.Form):
    
    birth_date= forms.DateField(initial="", widget=forms.SelectDateWidget(years=YEARS, attrs={'class': 'form-select form-select-lg mb-1'}))
