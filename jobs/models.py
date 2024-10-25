from django.db import models
from django.contrib.auth.models import User
from profile.models import Profile 


class JobType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True, help_text="Description du type de contrat")

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    contract_type = models.ForeignKey(JobType, on_delete=models.SET_NULL, null=True, related_name="jobs")
    required_skills = models.TextField(help_text="Liste des compétences requises")
    requirements = models.TextField(help_text="Conditions d'expérience, formation, etc.")
    published_date = models.DateTimeField(auto_now_add=True)
    employer = models.ForeignKey(User, on_delete=models.CASCADE)
    is_filled = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Application(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    application_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('submitted', 'Soumis'),
        ('reviewed', 'Examiné'),
        ('accepted', 'Accepté'),
        ('rejected', 'Rejeté'),
    ], default='submitted')

    def __str__(self):
        return f"Candidature de {self.profile.user.username} pour {self.job.title}"
