from django.contrib import admin
from django import forms
from .models import Company, Link, ApplicationStatus, JobApplication

class LinkForm(forms.ModelForm):
    url_type = forms.ChoiceField(choices=Link.URL_TYPES)
    url = forms.CharField()
    company = forms.ModelChoiceField(queryset=Company.objects.all())

class LinkAdminInline(admin.TabularInline):
    model = Link
    fields = ('url_type', 'url',)

class ApplicationStatusAdminInline(admin.TabularInline):
    model = ApplicationStatus

class ApplicationStatusAdmin(admin.ModelAdmin):
    pass

class CompanyAdmin(admin.ModelAdmin):
    inlines = (LinkAdminInline,)

#class JobApplicationForm(forms.ModelForm):
#

admin.site.register(Company, CompanyAdmin)
admin.site.register(JobApplication)
admin.site.register(ApplicationStatus, ApplicationStatusAdmin)
