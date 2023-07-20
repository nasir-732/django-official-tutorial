from django.shortcuts import Http404

from django.http import HttpResponse , HttpResponseRedirect

from django.template import loader

from django.shortcuts import get_object_or_404, render

from .models import Question , Choice

from django.urls import reverse

from django.utils import timezone

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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    
def newchoice(request,question_id):
        question=get_object_or_404(Question,pk=question_id)
        try:
           new_choice=request.POST["new_choice"]
           if not new_choice:
               raise KeyError
        except (KeyError):
           return render(
               request,
               "polls/addchoice.html",
               {
                  "question":question,
                  "error_message": "choice could not be added"
               },
           )
        else:
            newchoice=Choice(
               question=question,
               choice_text=new_choice
        )
            newchoice.save()
            return HttpResponseRedirect(reverse("polls:detail",args=(question.id,)))
        

def resetvote(request, question_id):
    # return HttpResponse("rest votes")
    question = get_object_or_404(Question, pk=question_id)
    for choice in question.choice_set.all():
        choice.votes = 0
        choice.save()
    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    
def addques(request):
    return render(request, "polls/addques.html")

def newques(request):
    try:
        new_question=request.POST["new_ques"]
        if not new_question:
            raise KeyError
    except(KeyError):
        return render(
            request,
            "polls/addques.html",
            {
                "error_message":"question could not be added",
            },
        )
    else:
        try:
            for question in Question.objects.all():
                if question.question_text == new_question:
                    raise KeyError
        except(KeyError):
            return render(
                request,
                "polls/addques.html",
                {
                    "error_message": "question already exits.",
                },
            )
        else:
            newquestion= Question(
                question_text = new_question,
                pub_date = timezone.now(),
                
            )
            newquestion.save()
            return HttpResponseRedirect(reverse("polls:index"))
        

