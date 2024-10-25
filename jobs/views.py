from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Job
from django.contrib import messages

class JobListView(View):
    def get(self, request):
        jobs = Job.objects.all()
        return render(request, 'job_list.html', {'jobs': jobs})

class JobDetailView(View):
    def get(self, request, pk):
        job = get_object_or_404(Job, pk=pk)
        return render(request, 'job_detail.html', {'job': job})

class JobApplyView(View):
    def get(self, request, pk):
        job = get_object_or_404(Job, pk=pk)
        return render(request, 'job_apply.html', {'job': job})

    def post(self, request, pk):
        job = get_object_or_404(Job, pk=pk)
        messages.success(request, 'Votre candidature a été envoyée avec succès !')
        return redirect('job_list')
