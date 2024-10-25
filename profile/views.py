from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserUpdateForm, ProfileUpdateForm
from ..profile.models import Profile

class ProfileView(LoginRequiredMixin, View):
    """
    ProfileView gère l'affichage et la mise à jour du profil de l'utilisateur.
    Attributs:
        login_url (str): URL de redirection pour la connexion si l'utilisateur n'est pas authentifié.
    Méthodes:
        get(request):
            Gère les requêtes GET pour afficher le profil de l'utilisateur.
            - Récupère ou crée un objet Profile pour l'utilisateur authentifié.
            - Initialise UserUpdateForm et ProfileUpdateForm avec les données de l'utilisateur.
            - Rendu du template 'profile.html' avec les formulaires.
        post(request):
            Gère les requêtes POST pour mettre à jour le profil de l'utilisateur.
            - Récupère ou crée un objet Profile pour l'utilisateur authentifié.
            - Initialise UserUpdateForm et ProfileUpdateForm avec les données soumises.
            - Valide et enregistre les formulaires s'ils sont valides.
            - Redirige vers la page de profil si la mise à jour est réussie.
            - Rendu du template 'profile.html' avec les formulaires si la mise à jour échoue.
    """
    login_url = '/login/'

    def get(self, request):
        profile, created = Profile.objects.get_or_create(user=request.user)
        
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=profile)

        return render(request, 'profile.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })

    def post(self, request):
        profile, created = Profile.objects.get_or_create(user=request.user)

        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()  
            profile_form.save()  
            return redirect('profile')  

        return render(request, 'profile.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })