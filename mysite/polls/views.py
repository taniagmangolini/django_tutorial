from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Question, Choice
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import QuestionSerializer, ChoiceSerializer

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list' : latest_question_list,
    }
    return HttpResponse(template.render(context, request))

"""
Outra versao:
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
"""


def detail(request, question_id):
    #se nao encontrar o obj, ja retorna o erro
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

"""
Outra versao:
def detail(request, question_id):
    try :
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist :
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question' : question})
"""

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows questions to be viewed or edited.
    """
    queryset = Question.objects.all().order_by('pub_date')
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class ChoiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows choices to be viewed or edited.
    """
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [permissions.IsAuthenticated]
