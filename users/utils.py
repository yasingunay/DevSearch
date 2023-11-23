from .models import Profile,Skill
from django.db.models import Q 



def searchProfiles(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    skills = Skill.objects.filter(name__icontains=search_query)

    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) | 
        Q(short_intro__icontains=search_query) |
        Q(skill__in= skills) )# filters the results to include only those that contain the specified value in a case-insensitive manner.
    return profiles, search_query