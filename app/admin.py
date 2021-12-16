from django.contrib import admin
from app.models import SAP  # модель из app


@admin.register(SAP)
class SAPAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'count',
        'date',
        'distance',
    )
    list_filter = (
        'name',
        'count',
        'date',
        'distance',
    )
    list_display_links = (
        'name',
        'count',
        'date',
        'distance',
    )
