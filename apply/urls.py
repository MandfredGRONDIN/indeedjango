from django.urls import path
from .views import JobApplyView, MyApplicationsView

urlpatterns = [
    path('my_apply/', MyApplicationsView.as_view(), name='my_applications'),
    path('apply/<int:pk>/', JobApplyView.as_view(), name='job_apply'),
]
