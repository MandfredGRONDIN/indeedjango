from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views import View
from .forms import UserRegistrationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import Profile

# Home View
class HomeView(LoginRequiredMixin, View):
    login_url = '/login/' 

    def get(self, request):
        return render(request, 'home.html')
    
# Register View
class RegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  
            user.save()
            login(request, user)  
            return redirect('home')  
        return render(request, 'register.html', {'form': form})

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
            - Affiche un message de succès et redirige vers la page de profil si la mise à jour est réussie.
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
            messages.success(request, 'Votre profil a été mis à jour avec succès.')
            return redirect('profile')  

        return render(request, 'profile.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })