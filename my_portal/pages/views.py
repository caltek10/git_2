from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')
def ded_moroz(request):
    return render(request, 'ded_moroz.html')