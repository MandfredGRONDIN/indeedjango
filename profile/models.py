from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Utilisateur")
    bio = models.TextField(blank=True, null=True, verbose_name="Biographie")
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Téléphone")
    is_available = models.BooleanField(default=True, verbose_name="Disponible")
    location = models.CharField(max_length=100, blank=True, null=True, verbose_name="Localisation")
    skills = models.TextField(blank=True, null=True, verbose_name="Compétences", help_text="Liste des compétences séparées par des virgules")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de mise à jour")

    def __str__(self):
        return f"Profil de {self.user.username}"

    def get_skills_list(self):
        """Retourne une liste des compétences sous forme de liste."""
        return [skill.strip() for skill in self.skills.split(',')] if self.skills else []

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profils"
        ordering = ['-created_at'] 
