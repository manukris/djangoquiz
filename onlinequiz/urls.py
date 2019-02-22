from django.urls import path,include
from .views import AddQuestion,ListQuestion

urlpatterns = [
    path('',ListQuestion.as_view(),name='questionlist'),
    path('add/',AddQuestion.as_view(),name="addquestion"),
]