from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Job
from apply.models import Application
from django.contrib.auth.mixins import LoginRequiredMixin
from profile.models import Profile 

class JobListView(LoginRequiredMixin, View):
    def get(self, request):
        profile = get_object_or_404(Profile, user=request.user)
        
        applied_jobs = Application.objects.filter(profile=profile).values_list('job_id', flat=True)
        
        jobs = Job.objects.filter(is_filled=False).exclude(id__in=applied_jobs)
        
        return render(request, 'job_list.html', {'jobs': jobs})

class JobDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        job = get_object_or_404(Job, pk=pk)
        profile = get_object_or_404(Profile, user=request.user)
        has_applied = Application.objects.filter(job=job, profile=profile).exists()
        return render(request, 'job_detail.html', {
            'job': job,
            'has_applied': has_applied
        })
