from django.shortcuts import render
from .models import MyJob


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    my_job = MyJob.objects.get(pk=2)
    return render(request, 'index.html', context={'my_job': my_job},)
