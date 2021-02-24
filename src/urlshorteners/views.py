import uuid

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Url


def index(request):
    return render(request, 'urlshorteners/index.html',  {
        'urls': Url.objects.all().order_by('id').reverse(),
    })


def new(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        uid = str(uuid.uuid4())[:5]

        new_url = Url(link=link, uuid=uid)
        new_url.save()

        return HttpResponse(uid)


def go(request, uid):
    url = get_object_or_404(Url, uuid=uid)
    return redirect(url.link)


def delete(request, id):
    url = get_object_or_404(Url, id=id)
    url.delete()

    return HttpResponse('Delete successfully.')
