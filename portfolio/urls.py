from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.project_list, name='project_list'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('projects/<int:pk>/interest/', views.add_interest, name='add_interest'),
    path('interests/', views.interest_list, name='interest_list'),
    path('ranking/', views.ranking_view, name='ranking_view'),
    path('evaluation_ranking/', views.evaluation_ranking, name='evaluation_ranking'),
]
