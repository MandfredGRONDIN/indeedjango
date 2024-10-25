from django.contrib import admin
from .models import Job, JobType, Application

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'employer', 'location', 'contract_type', 'is_filled', 'published_date')
    list_filter = ('is_filled', 'contract_type', 'published_date')
    search_fields = ('title', 'employer__username', 'location')
    date_hierarchy = 'published_date'
    ordering = ('-published_date',)
    list_editable = ('is_filled',)
    readonly_fields = ('published_date',)
    fieldsets = (
        ('Informations générales', {
            'fields': ('title', 'description', 'location', 'salary', 'contract_type', 'is_filled')
        }),
        ('Détails du poste', {
            'fields': ('required_skills', 'requirements')
        }),
        ('Informations de l\'employeur', {
            'fields': ('employer',),
        }),
        ('Date', {
            'fields': ('published_date',),
        }),
    )

class JobTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('profile', 'job', 'application_date', 'status')  
    search_fields = ('profile__user__username', 'job__title')
    list_filter = ('status',) 




admin.site.register(Job, JobAdmin)
admin.site.register(JobType, JobTypeAdmin)
admin.site.register(Application, ApplicationAdmin)
