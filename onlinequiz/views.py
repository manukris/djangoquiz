from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView
from .models import Questions

# Create your views here.

class AddQuestion(CreateView):
    model = Questions
    fields = ['question','option1','option2','option3','option4','option1','rightop']

class ListQuestion(ListView):
    model = Questions
    template_name = 'onlinequiz/list.html'

class EditQuestions(UpdateView):
    model = Questions
    fields = ['question', 'option1', 'option2', 'option3', 'option4', 'option1', 'rightop']

