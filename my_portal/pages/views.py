from django.shortcuts import render
from django.conf import settings
import os
from pages.models import Pages, Comment
from pages.forms import CommentForm
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
User = get_user_model()



def index(request, page_id):

    page = Pages.objects.get(pk=page_id)
    comments = Comment.objects.filter(page=page).order_by('pk')
    context = {
        'page': page,
        'comments': comments
               }
    return render(request, 'index.html', context=context)

def static_page(request):
    form = CommentForm()
    context ={
        'form': form
    }
    return render(request, 'static_page.html', context=context)

def create_comment(request):
    context = {}
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            print('vse ok')
        else:
            print('form not valied')
        context['form'] = form
    return render(request, 'create_comment.html', context=context)

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