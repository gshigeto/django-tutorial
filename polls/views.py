from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse

from .models import Question


def index(req):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(req, 'polls/index.html', context)


def detail(req, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(req, 'polls/detail.html', {'question': question})


def results(req, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(req, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
