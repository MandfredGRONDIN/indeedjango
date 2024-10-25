from django.contrib import admin
from django.contrib import messages
from .models import Job, JobType

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'employer', 'location', 'contract_type', 'is_filled', 'published_date')
    list_filter = ('is_filled', 'contract_type', 'published_date')
    search_fields = ('title', 'employer__username', 'location')
    date_hierarchy = 'published_date'
    ordering = ('-published_date',)
    list_editable = ('is_filled',)
    readonly_fields = ('published_date',)
    
    actions = ['mark_as_filled', 'mark_as_unfilled']

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

    def mark_as_filled(self, request, queryset):
        updated_count = queryset.update(is_filled=True)
        self.message_user(request, f"{updated_count} contrat(s) marqué(s) comme pourvu(s).", messages.SUCCESS)

    mark_as_filled.short_description = "Marquer comme pourvu"

    def mark_as_unfilled(self, request, queryset):
        updated_count = queryset.update(is_filled=False)
        self.message_user(request, f"{updated_count} contrat(s) marqué(s) comme non pourvu(s).", messages.SUCCESS)

    mark_as_unfilled.short_description = "Marquer comme non pourvu"

class JobTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

admin.site.register(Job, JobAdmin)
admin.site.register(JobType, JobTypeAdmin)
