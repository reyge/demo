from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from . import views


@login_required(login_url='login')
def interest(request):
    form = InterestForm()
    if request.method == 'POST':
        form = InterestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'ad/interest.html', {'form': form})


@login_required(login_url='login')
def language(request):
    form = LanguageForm()
    if request.method == 'POST':
        form = LanguageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'ad/language.html', {'form': form})


@login_required(login_url='login')
def info(request):

    xxx = Myinfo.objects.get(id=1)
    form = MyinfoForm(instance=xxx)

    if request.method == 'POST':
        form = MyinfoForm(request.POST, instance=xxx)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'ad/info.html', {'form': form})


@login_required(login_url='login')
def dashboard(request):
    # return HttpResponse('Hi i am learning aws')
    return render(request, 'ad/index.html')
# Create your views here.


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')  # gets username without any attribues cleaned_data
                messages.success(request, 'Account was created for ' + user)
                return HttpResponse('login')
        context = {'form': form}
        return render(request, 'ad/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/ad')
            else:
                messages.info(request, 'Username or password is incorrect')

        return render(request, 'ad/login.html')


def logoutUser(request):
    logout(request)
    return redirect('/login')


