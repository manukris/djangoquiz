from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView,ListView,UpdateView,FormView,DeleteView
from .models import Questions
from .form import LoginForm
from .models import Movie

# Create your views here.




class AddQuestion(CreateView):
    model = Questions
    fields = ['question','option1','option2','option3','option4','option1','rightop']





