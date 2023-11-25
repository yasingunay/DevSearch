from django.urls import path
from . import views


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("users/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("users/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", views.getRoutes),
    path("projects/", views.getProjets),
    path("projects/<str:pk>/", views.getProjet),
    path("projects/<str:pk>/vote/", views.projectVote),
    path("remove-tag/", views.removeTag),
]
