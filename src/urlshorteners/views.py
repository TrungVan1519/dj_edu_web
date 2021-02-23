from django.shortcuts import render, redirect
from django.http import HttpResponse

from . import models

import uuid


def index(request):
    return render(request, 'urlshorteners/index.html',  {
        'urls': models.Url.objects.all().order_by('id').reverse(),
    })


def new(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        uid = str(uuid.uuid4())[:5]

        new_url = models.Url(link=link, uuid=uid)
        new_url.save()

        return HttpResponse(uid)


def go(request, uid):
    url = models.Url.objects.get(uuid=uid)
    return redirect(url.link)
