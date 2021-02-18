from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from .models import *


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html', locals())


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', locals())


def results(request, question_id):
    response = "You are looking  at the of question %s. "
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse(f"You are voting on question {question_id}")