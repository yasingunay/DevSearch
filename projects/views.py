from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from . models import Project, Tag
from .forms import ProjectForm
from.utils import searchProjects



def projects(request):
    projects, search_query = searchProjects(request)

    page = request.GET.get('page')
    results = 3 
    p = Paginator(projects , results)

    try:
        projects = p.page(page)
    except PageNotAnInteger: # if page is not passed in
        page = 1 
        projects = p.page(page)
    except EmptyPage: # if user goes to a page does exist like 10000... 
        page = p.num_pages # return last page
        projects = p.page(page)


    context = {'projects': projects, 'search_query' : search_query}
    return render(request, 'projects/projects.html', context )

def project(request, pk):
    projectObj = Project.objects.get(id = pk)
    return render(request, 'projects/single-project.html', {'project': projectObj})

@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES )
        if form.is_valid():
            project = form.save(commit=False) # does not save it to the database immediately
            project.owner  = profile
            project.save()
            return redirect('account')



    context = {'form': form}
    return render(request, "projects/project_form.html", context)


@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id = pk)
    form = ProjectForm(instance = project)

    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('account')



    context = {'form': form}
    return render(request, "projects/project_form.html", context)


@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id = pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    context = {'object': project}
    return render(request, "delete_template.html", context)