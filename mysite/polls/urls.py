from django.urls import path


from .import views
app_name ="polls"
urlpatterns=[
    path("", views.index, name="index"),
     path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/votes/", views.vote, name="vote"),

    path("<int:question_id>/newchoice/", views.newchoice, name="newchoice"),

    path("<int:question_id>/newchoice/", views.newchoice, name="newchoice"),

    path("<int:question_id>/resetvote/", views.resetvote, name="resetvote"),

    path("addques/", views.addques, name="addques"),

    path("newques/", views.newques, name="newques"),

]
    

