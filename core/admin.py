from django.contrib import admin

from .models import Job


class JobAdmin(admin.ModelAdmin):
    model = Job
    list_display = ["title"]
    search_fields = ["title"]


admin.site.register(Job, JobAdmin)
