from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import  Application
from jobs.models import Job
from django.contrib.auth.mixins import LoginRequiredMixin
from profile.models import Profile 

class MyApplicationsView(LoginRequiredMixin, View):
    def get(self, request):
        profile = get_object_or_404(Profile, user=request.user)
        applications = Application.objects.filter(profile=profile)
        return render(request, 'my_apply.html', {'applications': applications})

class JobApplyView(LoginRequiredMixin, View):
    def get(self, request, pk):
        job = get_object_or_404(Job, pk=pk)
        return render(request, 'job_apply.html', {'job': job})

    def post(self, request, pk):
        job = get_object_or_404(Job, pk=pk)
        profile = get_object_or_404(Profile, user=request.user)  

        Application.objects.create(profile=profile, job=job)

        return redirect('job_list')