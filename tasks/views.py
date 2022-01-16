from math import pi
import django
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, HttpResponse
import datetime
from .models import User, Task


def index(request):
    return render(request, 'tasks/index.html')


def sign_up(request):
    params = {
        key: request.POST.get(key)
        for key in ['username', 'password']
    }

    try:
        user = User(**params)
        user.save()
    except django.db.utils.IntegrityError:
        pass

    return redirect('/')


def sign_in(request):
    params = {
        key: request.POST.get(key)
        for key in ['username', 'password']
    }

    print(User.objects.filter(**params).count(), params)

    if User.objects.filter(**params).count():
        current_user = User.objects.filter(**params).first()
        response = redirect('/tasks/tasks')
        response.set_cookie('username', current_user.username)
        return response
    else:
        return redirect('/')


def task(request):
    tasks = Task.objects.all()
    current_user = User.objects.get(username=request.COOKIES.get('username'))

    return render(request, 'tasks/tasks.html', {
        'tasks': tasks,
        'current_user': current_user,
    })


def add(request):
    params = {
        key: request.POST.get(key)
        for key in ['title', 'description']
    }

    try:
        params['deadline'] = datetime.datetime.strptime(
            request.POST.get('deadline'), '%b %d, %Y')
    except:
        pass

    task_owner = User.objects.get(username=request.COOKIES.get('username'))
    Task.objects.create(**params, user=task_owner)

    return redirect('/tasks/tasks')


class TaskView(DetailView):
    model = Task
    template_name = 'tasks/detail.html'

    # def get(self, *args, **kwargs):
    #     task = Task.objects.get(id=kwargs.get('id'))
    #     print(task)
    #     return HttpResponse('a')
    # return render()
