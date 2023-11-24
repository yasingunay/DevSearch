from django.urls import path
from. import views

urlpatterns = [
    path('', views.getRoutes),
    path('projects/', views.getProjets),
    path('projects/<str:pk>/', views.getProjet)
]