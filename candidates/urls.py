from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_candidate, name='register_candidate'),
    path('list/', views.list_candidates, name='list_candidates'),
    path('download/<int:candidate_id>/', views.download_resume, name='download_resume'),
]
