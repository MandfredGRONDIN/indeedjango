from django.db import models
from django.contrib.auth.models import User
from profile.models import Profile 
from jobs.models import Job

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
