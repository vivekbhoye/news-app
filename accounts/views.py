from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,DeleteView
from .models import CustomUser
from .forms import CustomUserCreationForm

# Create your views here.
# class HomeListView(ListView):
#     model = 

# def home(request):
#     return render(request,'home.html')

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'