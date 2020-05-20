from django.shortcuts import render
from django.conf import settings
import os
from pages.models import Pages



def index(request):
    me_pages = Pages.objects.all()
    context = {"pages": me_pages}
    return render(request, 'index.html', context=context)
def ded_moroz(request):
    my_list = [
        "Строка1", "Строка2", "Строка3", 1, 123, 1233, "Последняя строка"
    ]
    my_articles=[]
    my_dict = {"title": "Статья1", "text": "<b>Жирные слова</b>,продолжение тескта обыкновенным шрифтом" }

    context = {
        "title":"Страница1",
        "list_of_strings": my_list,
        "list_of_articles": my_articles,
        "my_dict": my_dict
    }
    return render(request, 'ded_moroz.html', context=context)