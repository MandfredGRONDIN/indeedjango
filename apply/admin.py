from django.contrib import admin
from .models import Application
from django.contrib import messages

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('profile', 'job', 'application_date', 'status')  
    search_fields = ('profile__user__username', 'job__title')
    list_filter = ('status',) 
    
    actions = ['mark_as_submitted', 'mark_as_reviewed', 'mark_as_accepted', 'mark_as_rejected']

    def mark_as_submitted(self, request, queryset):
        updated_count = queryset.update(status='submitted')
        self.message_user(request, f"{updated_count} candidature(s) marquée(s) comme soumise(s).", messages.SUCCESS)

    mark_as_submitted.short_description = "Marquer comme soumise"

    def mark_as_reviewed(self, request, queryset):
        updated_count = queryset.update(status='reviewed')
        self.message_user(request, f"{updated_count} candidature(s) marquée(s) comme examinée(s).", messages.SUCCESS)

    mark_as_reviewed.short_description = "Marquer comme examinée"

    def mark_as_accepted(self, request, queryset):
        updated_count = queryset.update(status='accepted')
        self.message_user(request, f"{updated_count} candidature(s) marquée(s) comme acceptée(s).", messages.SUCCESS)

    mark_as_accepted.short_description = "Marquer comme acceptée"

    def mark_as_rejected(self, request, queryset):
        updated_count = queryset.update(status='rejected')
        self.message_user(request, f"{updated_count} candidature(s) marquée(s) comme refusée(s).", messages.SUCCESS)

    mark_as_rejected.short_description = "Marquer comme refusée"

admin.site.register(Application, ApplicationAdmin)
