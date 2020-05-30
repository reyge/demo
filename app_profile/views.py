from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
import base64


def home(request):
    myinfo = Myinfo.objects.get(id=1)
    img = base64.b64encode(myinfo.picture)
    language = Language.objects.all()
    interest = Interest.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    skill = Skills.objects.all()

    # return HttpResponse('Hi i am learning aws')
    context = {'myinfo': myinfo, 'language': language, 'interest': interest, 'education': education,
               'experience': experience, 'skill': skill}

    return render(request, 'dashboard.html', context)
# Create your views here.




