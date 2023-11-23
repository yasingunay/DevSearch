from .models import Project, Tag
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginateProjets(request, projects, results):
    page = request.GET.get("page")
    p = Paginator(projects, results)

    try:
        projects = p.page(page)
    except PageNotAnInteger:  # if page is not passed in
        page = 1
        projects = p.page(page)
    except EmptyPage:  # if user goes to a page does exist like 10000...
        page = p.num_pages  # return last page
        projects = p.page(page)

    leftIndex = int(page) - 4
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = int(page) + 5

    if rightIndex > p.num_pages:
        rightIndex = p.num_pages + 1

    custom_range = range(leftIndex, rightIndex)
    return custom_range, projects


def searchProjects(request):
    search_query = ""

    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")

    tags = Tag.objects.filter(name__icontains=search_query)

    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query)
        | Q(description__icontains=search_query)
        | Q(owner__name__icontains=search_query)
        | Q(tags__in=tags)
    )

    return projects, search_query
