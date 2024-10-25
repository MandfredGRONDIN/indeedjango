from django.contrib import admin
from .models import Application

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('profile', 'job', 'application_date', 'status')  
    search_fields = ('profile__user__username', 'job__title')
    list_filter = ('status',) 


admin.site.register(Application, ApplicationAdmin)
