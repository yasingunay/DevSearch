from .models import Profile, Skill
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginateProfiles(request, profiles, results):
    page = request.GET.get("page")
    p = Paginator(profiles, results)

    try:
        profiles = p.page(page)
    except PageNotAnInteger:  # if page is not passed in
        page = 1
        profiles = p.page(page)
    except EmptyPage:  # if user goes to a page does exist like 10000...
        page = p.num_pages  # return last page
        profiles = p.page(page)

    leftIndex = int(page) - 1
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = int(page) + 3

    if rightIndex > p.num_pages:
        rightIndex = p.num_pages + 1

    custom_range = range(leftIndex, rightIndex)
    return custom_range, profiles


def searchProfiles(request):
    search_query = ""

    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")

    skills = Skill.objects.filter(name__icontains=search_query)

    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query)
        | Q(short_intro__icontains=search_query)
        | Q(skill__in=skills)
    )  # filters the results to include only those that contain the specified value in a case-insensitive manner.
    return profiles, search_query
