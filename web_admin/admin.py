from django.contrib import admin

# Register your models here.
from web_admin.models import New


@admin.register(New)
class AdminNew(admin.ModelAdmin):
    list_display = ['date',
                    'subject',
                    'content',
                    'user']

    search_fields = ('subject',)
