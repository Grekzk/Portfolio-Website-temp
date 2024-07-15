from django.shortcuts import render
from .models import Project, Experience, Education, ProfessionalSkills, Languages


def index(request):
    return render(request, template_name='pfapp/index.html')


def resume(request):
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    prof_skills = ProfessionalSkills.objects.all()
    languages = Languages.objects.all()
    context = {
        'exp_s': experiences,
        'edu_s': educations,
        'skills': prof_skills,
        'languages': languages,
    }
    return render(request, 'pfapp/resume.html', context)


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
