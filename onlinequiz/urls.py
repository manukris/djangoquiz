from django.urls import path,include
from .views import AddQuestion,ListQuestion,EditQuestions,Addmovie,Deletemovie

urlpatterns = [
    path('',ListQuestion.as_view(),name = 'movielist'),
    path('add/',AddQuestion.as_view(),name = "addquestion"),
    path('edit/<int:pk>',EditQuestions.as_view(),name = "edit"),
    path('moviee',Addmovie.as_view(),name = 'addmovie'),
    path('delmovie/<int:pk>/',Deletemovie.as_view(),name = 'deletemovie'),
   # path('login/',)
]