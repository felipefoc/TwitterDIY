from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
class LoginHome(View):
    template_name = 'login.html'
     
    def get(self, request):
        # logic
        return render(request, self.template_name)

    