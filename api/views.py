from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import ProjectSerializer
from projects.models import Project, Review


@api_view(['GET'])
def getRoutes(request):

    routes =[
        {'GET': '/api/projects'},
        {'GET': '/api/projects/id'},
        {'POST': '/api/projects/id/vote'},

        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},
    ]

    return Response(routes)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getProjets(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def getProjet(request, pk):
    project = Project.objects.get(id= pk)
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated]) # we need a valid token to user can vote
def projectVote(request, pk):
    project = Project.objects.get(id = pk)
    user =request.user.profile # This user is coming from token not session because of the @api_view decorator
    data = request.data

    review, created  = Review.objects.get_or_create(
        owner = user,
        project = project,
    )

    review.value = data['value']
    review.save()
    project.getVoteCount # because of it is @property decoretor we dont have to trigger a typical funtion

    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)