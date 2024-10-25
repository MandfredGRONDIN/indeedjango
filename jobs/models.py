from django.db import models
from django.contrib.auth.models import User

class JobType(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nom")
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Description du type de contrat",
        verbose_name="Description"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Type de contrat"
        verbose_name_plural = "Types de contrat"

class Job(models.Model):
    title = models.CharField(max_length=255, verbose_name="Titre")
    description = models.TextField(verbose_name="Description")
    location = models.CharField(max_length=100, verbose_name="Lieu")
    salary = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Salaire"
    )
    contract_type = models.ForeignKey(
        JobType,
        on_delete=models.SET_NULL,
        null=True,
        related_name="jobs",
        verbose_name="Type de contrat"
    )
    required_skills = models.TextField(
        help_text="Liste des compétences requises", verbose_name="Compétences requises"
    )
    requirements = models.TextField(
        help_text="Conditions d'expérience, formation, etc.", verbose_name="Exigences"
    )
    published_date = models.DateTimeField(auto_now_add=True, verbose_name="Date de publication")
    employer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Employeur")
    is_filled = models.BooleanField(default=False, verbose_name="Est pourvu")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Offre d'emploi"
        verbose_name_plural = "Offres d'emploi"
