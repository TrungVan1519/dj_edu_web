from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from . import models


def index(request):
    return render(request, 'notebooks/index.html', {
        'notes': models.Note.objects.all().order_by('id').reverse(),
    })


def new(request):
    if request.method == 'POST':
        new_note = models.Note(content=request.POST.get('content'))
        new_note.save()

        return HttpResponse('Save successfully')


def update(request, id):
    if request.method == 'POST':
        note = get_object_or_404(models.Note, id=id)
        note.content = request.POST.get('content')
        note.save()

        return HttpResponse('Update successfully')


def delete(request, id):
    note = get_object_or_404(models.Note, id=id)
    note.delete()

    return redirect('/notebooks/')
