from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from mypoll.models import Question


def index(request):
    last_questions = list(Question.objects.all())

    return render(request, 'mypoll/index.html', {'questions': last_questions}, request)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)