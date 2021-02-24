# core libs
import json

# pip libs
from PyDictionary import PyDictionary

# django libs
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404

# custom libs
from .models import Word


def index(request):
    return render(request, 'dictionaries/index.html', {
        'words': Word.objects.all().order_by('id').reverse(),
    })


def search(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword')

        return JsonResponse({
            'keyword': keyword,
            'meaning': PyDictionary().meaning(keyword),
            'synonym': PyDictionary().synonym(keyword),
            'antonym': PyDictionary().antonym(keyword),
        })


def new(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword')

        try:
            word = Word.objects.get(keyword=keyword)
            return HttpResponse(f'Keyword \'{word.keyword }\' is already saved.')
        except Word.DoesNotExist:
            meaning = request.POST.get('meaning')
            synonym = request.POST.get('synonym')
            antonym = request.POST.get('antonym')

            if not meaning and not synonym and not antonym:
                if not PyDictionary().meaning(keyword):
                    return HttpResponse(f'{keyword} is meaningless. Please try again.')

                noun = PyDictionary().meaning(keyword).get('Noun')
                meaning += (f'- Noun: {str(noun)[1:-1]}' + '\n' if noun else '').replace('\'', '')

                verb = PyDictionary().meaning(keyword).get('Verb')
                meaning += (f'- Verb: {str(verb)[1:-1]}' if verb else '').replace('\'', '')

                syno = PyDictionary().synonym(keyword)
                synonym = str(syno)[1:-1].replace('\'', '') if syno else ''

                anto = PyDictionary().antonym(keyword)
                antonym = str(anto)[1:-1].replace('\'', '') if anto else ''

            new_word = Word(keyword=keyword, meaning=meaning,
                            synonym=synonym, antonym=antonym)
            new_word.save()

            return HttpResponse('Save successfully.')


def delete(request, id):
    word = get_object_or_404(Word, id=id)
    word.delete()

    return HttpResponse('Delete successfully.')
