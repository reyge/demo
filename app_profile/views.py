from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


def home(request):
    myinfo = Myinfo.objects.get(id=1)
    # return HttpResponse('Hi i am learning aws')
    context = {'myinfo': myinfo}

    return render(request, 'dashboard.html', context)
# Create your views here.




