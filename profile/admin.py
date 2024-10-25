from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'phone', 'is_available', 'location', 'created_at')  
    search_fields = ('user__username', 'user__email', 'bio', 'phone', 'skills')  
    list_filter = ('user__is_active', 'user__is_staff', 'is_available')
    ordering = ('-created_at',)  

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profils'
    fields = ('bio', 'phone', 'is_available', 'location') 
    extra = 0  

class UserAdmin(admin.ModelAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
