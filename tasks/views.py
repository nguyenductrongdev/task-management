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


class IndexView(ListView):
    model = Task
    template_name = 'tasks/tasks.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.all()


class TaskView(DetailView):
    model = Task
    template_name = 'tasks/detail.html'
    context_object_name = 'task'
