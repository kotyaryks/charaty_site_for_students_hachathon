from django.http import HttpResponse
from django.template import loader

from .models import Post, Project, TeamMember, Shelter, Report


def blog(request):
    post = Post.objects.all()
    context = {
        'post_list': post,
    }
    template = loader.get_template('blogs.html')
    return HttpResponse(template.render(context, request))


def home(request):
    context = {
    }
    template = loader.get_template('donate.html')
    return HttpResponse(template.render(context, request))


def projects(request):
    project = Project.objects.all()

    context = {
        'projects_list': project,
    }
    template = loader.get_template('projects.html')
    return HttpResponse(template.render(context, request))


def team(request):
    team = TeamMember.objects.all()

    context = {
        'team_list': team,
    }
    template = loader.get_template('team.html')
    return HttpResponse(template.render(context, request))


def shelters(request):
    shelters = Shelter.objects.all()

    context = {
        'shelter_list': shelters,
    }
    template = loader.get_template('Shelters.html')
    return HttpResponse(template.render(context, request))


def reports(request):
    reports = Report.objects.all()

    context = {
        'reports_list': reports,
    }
    template = loader.get_template('reports.html')
    return HttpResponse(template.render(context, request))
