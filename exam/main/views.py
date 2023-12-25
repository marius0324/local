from django.views.generic import CreateView, ListView

from .models import Product
from .forms import ProductForm
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from .forms import RegisterForm





class BBLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'main/logout.html'
    success_url = reverse_lazy('home')


class BBLoginView(LoginView):
    template_name = 'main/login.html'
    success_url = reverse_lazy('home')


def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')


class CreateProduct(CreateView):
    model = Product
    template_name = 'main/add_service.html'
    success_url = reverse_lazy('home')
    form_class = ProductForm


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        AdvUser = authenticate(request, username=username, password=password)
        if AdvUser is not None:
            login(request, AdvUser)
            return redirect('add_service')
    return render(request, 'main/login.html')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'main/register_user.html', {'form': form})


class ListProduct(ListView):
    model = Product
    template_name = 'main/services.html'
    context_object_name = 'products'