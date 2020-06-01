from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *



def home(request):
    context = mainn(request)

    return render(request, 'dashboard.html', context)


def mainn(request):
    myinfo = Myinfo.objects.get(id=1)
    language = Language.objects.all()
    interest = Interest.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    skill = Skills.objects.all()

    # return HttpResponse('Hi i am learning aws')
    context = {'myinfo': myinfo, 'language': language, 'interest': interest, 'education': education,
               'experience': experience, 'skill': skill}
    return context


def portfolio(request):

    context = mainn(request)
    return render(request, 'portfolio.html', context)
# Create your views here.




