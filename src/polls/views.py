from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse

from .models import Question, Choice


def index(request):
    return render(request, 'polls/index.html', {
        'questions': Question.objects.all().order_by('pub_date').reverse(),
    })


def vote(request, id):
    question = get_object_or_404(Question, id=id)

    if request.method == 'POST':
        try:
            selected_choice = question.choice_set.get(
                pk=request.POST.get('choice'))
            selected_choice.votes += 1
            selected_choice.save()

            return redirect(reverse('polls:detail', args=(question.id,)))
        except (KeyError, Choice.DoesNotExist):
            return render(request, 'polls/vote.html', {
                'question': question,
                'error_message': "You didn't select a choice.",
            })

    return render(request, 'polls/vote.html', {
        'question': question,
    })


def detail(request, id):
    question = get_object_or_404(Question, id=id)
    return render(request, 'polls/detail.html', {
        'question': question,
    })
