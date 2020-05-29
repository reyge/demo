from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


def home(request):
    myinfo = Myinfo.objects.get(id=1)
    language = Language.objects.all()
    interest = Interest.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()

    # return HttpResponse('Hi i am learning aws')
    context = {'myinfo': myinfo, 'language': language, 'interest': interest, 'education': education,
               'experience': experience}

    return render(request, 'dashboard.html', context)
# Create your views here.




