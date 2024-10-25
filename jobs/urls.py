from django.urls import path
from .views import JobListView, JobDetailView

urlpatterns = [
    path('job/', JobListView.as_view(), name='job_list'),
    path('job/<int:pk>/', JobDetailView.as_view(), name='job_detail'),
]
