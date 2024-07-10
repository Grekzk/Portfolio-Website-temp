from django.shortcuts import render


def index(request):
    return render(request, template_name='pfapp/index.html')


def services(request):
    return render(request, template_name='pfapp/services.html')


def resume(request):
    return render(request, template_name='pfapp/resume.html')


def work(request):
    return render(request, template_name='pfapp/work.html')


def contact(request):
    return render(request, template_name='pfapp/contact.html')
