from django.shortcuts import render
from .models import Project


def index(request):
    return render(request, template_name='pfapp/index.html')


def resume(request):
    return render(request, template_name='pfapp/resume.html')


def work(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'pfapp/work.html', context)


def contact(request):
    return render(request, template_name='pfapp/contact.html')


def privacy(request):
    return render(request, template_name='pfapp/privacy.html')
