from django.http import HttpResponse
from django.shortcuts import render


def homePage(request):
    # return HttpResponse('homePage')
    return render(request, 'homepage.html')

def about(request):
    # return HttpResponse('about')
    return render(request, 'about.html')
