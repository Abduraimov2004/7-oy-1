from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib import messages
from .models import User


class HomePageView(View):
    def get(self, request):
        return render(request, 'index.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        phone = request.POST.get('phone')

        if password != password_confirm:
            messages.warning(request, 'Password confirmation is incorrect')
            return redirect(reverse('main:register'))

        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Username already exists')
            return redirect(reverse('main:register'))

        if User.objects.filter(email=email).exists():
            messages.warning(request, 'Email already exists')
            return redirect(reverse('main:register'))

        if User.objects.filter(phone=phone).exists():
            messages.warning(request, 'Phone already exists')
            return redirect(reverse('main:register'))

        User.objects.create_user(username=username, email=email, password=password, phone=phone)
        messages.success(request, 'Registration successful! You can now log in.')
        return redirect(reverse('main:login'))


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')


        if not User.objects.filter(username=username).exists():
            messages.warning(request, 'Username does not exist')
            return redirect(reverse('main:login'))


        if User.objects.filter(password=password).exists():
            messages.warning(request, 'Password is incorrect')
            return redirect(reverse('main:login'))

        User.objects.filter(username=username).update(password=password)
        messages.success(request, 'Login successful!')
        return redirect(reverse('main:login'))




