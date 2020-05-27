from django.shortcuts import render
from django.http import HttpResponse


def employee_list(request):
    # return HttpResponse('Hi i am learning aws')
    return render(request, 'dashboard.html')
# Create your views here.
