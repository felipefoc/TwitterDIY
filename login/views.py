from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import UserForm

# Create your views here.
class LoginHome(View):
    template_name = 'login.html'
    form_class = UserForm
    initial = {'key': 'value'}
     
    def get(self, request):
        form = self.form_class(initial=self.initial)
        
        return render(request, self.template_name, {'form' : form})

    