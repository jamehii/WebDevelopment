from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect

from django.urls import reverse
from django.template import loader
from django.views import generic
from django.utils import timezone

from .models import Choice, Question


class IndexView(generic.ListView):
    """ 
    
    'model' attribute is not set to 'Question'
    If model = Question, then the context will be = question
    but we don't want 'question', we want 'latest_question_list'
    we provide our own context name with: context_object_name
    
    """
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    # override this function to return "list of data" back to context_object_name = 'latest_question_list'
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """

        return Question.objects.filter(pub_date__lte = timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
 
    # Notes: the name of the "context" will be = question ( follow model name )
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.

        return render(
            request,
            'polls/detail.html',
            { 'question':question, 'error_message': "You didn't select a choice."}
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect( reverse('polls:results', args = (question.id,)) )





# Replaced by class IndexView()
"""
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
"""

# Replaced by class DetailView()

"""
def detail(request, question_id):

    '''
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    '''

    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/detail.html', {'question':question})
"""

# Replaced by class ResultsView()

"""
def results(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    return render( request, "polls/results.html", {'question':question} )
"""