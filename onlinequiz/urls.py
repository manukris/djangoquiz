from django.urls import path,include
from .views import AddQuestion,ListQuestion,EditQuestions

urlpatterns = [
    path('',ListQuestion.as_view(),name = 'questionlist'),
    path('add/',AddQuestion.as_view(),name = "addquestion"),
    path('edit/<int:pk>',EditQuestions.as_view(),name = "editquestion"),
   # path('login/',)
]