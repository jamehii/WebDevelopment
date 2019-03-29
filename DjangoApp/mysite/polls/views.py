from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Question
from django.template import loader


def index(request):

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    '''
    Use template loader
    ====================

    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }

    return HttpResponse(template.render(context, request))
    '''

    # Here use shortcuts: render()
    context = {
        'latest_question_list': latest_question_list,
    }

    return render(request, 'polls/index.html', context)


def detail(request, question_id):

    try:
        question = Quetion.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, 'polls/detail.html', {'question':question})


def results(request, question_id):

    response = "You're looking at the results of the question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):

    return HttpResponse("You're voting on question %s." % question_id)