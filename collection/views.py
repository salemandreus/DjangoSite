from __future__ import unicode_literals

from django.shortcuts import render
from collection.models import Day

def index(request):
    days = Day.objects.all()

    return render(request, 'index.html', {
        'days': days,
    })
