from django.shortcuts import Http404

from django.http import HttpResponse

from django.template import loader

from django.shortcuts import get_object_or_404, render

from .models import Question



def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    data={"question_list": latest_question_list}
    return render(request,"polls/index.html",data)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response=f"you are looking at the result of question {question_id}"
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f"you are looking for reponse {question_id}")
