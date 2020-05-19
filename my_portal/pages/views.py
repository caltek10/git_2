from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    name = request.GET.get('name')
    context={"name": name}
    return render(request, 'index.html', context=context)
