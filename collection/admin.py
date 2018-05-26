from __future__ import unicode_literals

from django.contrib import admin
from collection.models import Day

class DayAdmin(admin.ModelAdmin):
    model = Day
    list_display = ('date', 'day', 'hightemp', 'lowtemp', 'wind', 'rain')
    prepopulated_fields = {'slug': ('day',)}

admin.site.register(Day, DayAdmin)
