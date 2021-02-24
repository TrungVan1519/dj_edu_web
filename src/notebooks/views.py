from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Note


def index(request):
    return render(request, 'notebooks/index.html', {
        'notes': Note.objects.all().order_by('id').reverse(),
    })


def new(request):
    if request.method == 'POST':
        new_note = Note(content=request.POST.get('content'))
        new_note.save()

        return HttpResponse('Save successfully.')


def update(request, id):
    if request.method == 'POST':
        note = get_object_or_404(Note, id=id)
        note.content = request.POST.get('content')
        note.save()

        return HttpResponse('Update successfully.')


def delete(request, id):
    note = get_object_or_404(Note, id=id)
    note.delete()

    return HttpResponse('Delete successfully.')
