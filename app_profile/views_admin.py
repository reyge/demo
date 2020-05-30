from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from . import views



@login_required(login_url='login')
def delete_experience(request):
    if request.method == 'POST':

        id = request.POST.get('del_a')
        experience = Experience.objects.get(pk=id)
        experience.delete()
        return redirect('/experience')


@login_required(login_url='login')
def experience(request, id=0):
    if request.method == "GET":

        if id == 0:
            experience = Experience.objects.all()
            form = ExperienceForm()  # create object form and assign instance of model form
        else:
            experience= Experience.objects.get(pk=id)
            form = ExperienceForm(instance=experience)
            experience= Experience.objects.all()
        return render(request, 'ad/experience.html', {'form': form, 'experience': experience})
    else:

        if id == 0:
            form = ExperienceForm(request.POST)
        else:
            experience= Experience.objects.get(pk=id)
            form = ExperienceForm(request.POST, instance=experience)
        form.save()

        return redirect('/experience')



@login_required(login_url='login')
def delete_education(request):
    if request.method == 'POST':

        id = request.POST.get('del_a')
        education = Education.objects.get(pk=id)
        education.delete()
        return redirect('/education')


@login_required(login_url='login')
def education(request, id=0):
    if request.method == "GET":

        if id == 0:
            education = Education.objects.all()
            form = EducationForm()  # create object form and assign instance of model form
        else:
            education = Education.objects.get(pk=id)
            form = EducationForm(instance=education)
            education = Education.objects.all()
        return render(request, 'ad/education.html', {'form': form, 'education': education})
    else:

        if id == 0:
            education = Education.objects.all()
            form = EducationForm(request.POST)
        else:
            education = Education.objects.get(pk=id)
            form = EducationForm(request.POST, instance=education)
        form.save()

        return redirect('/education')



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
        form = MyinfoForm(request.POST, request.FILES, instance=xxx)
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


