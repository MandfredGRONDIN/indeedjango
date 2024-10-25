from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Job, Application
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from authentification.models import Profile 

class JobListView(LoginRequiredMixin, View):
    def get(self, request):
        jobs = Job.objects.all()
        return render(request, 'job_list.html', {'jobs': jobs})

class JobDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        job = get_object_or_404(Job, pk=pk)
        return render(request, 'job_detail.html', {'job': job})

class JobApplyView(LoginRequiredMixin, View):
    def get(self, request, pk):
        job = get_object_or_404(Job, pk=pk)
        return render(request, 'job_apply.html', {'job': job})

    def post(self, request, pk):
        job = get_object_or_404(Job, pk=pk)
        profile = get_object_or_404(Profile, user=request.user)  

        Application.objects.create(profile=profile, job=job)

        return redirect('job_list')
