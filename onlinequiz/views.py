from django.shortcuts import render
from django.views.generic import CreateView
from .models import Questions

# Create your views here.
def index(request):
    return render(request,'onlinequiz/add.html')

class AddQuestion(CreateView):
    model = Questions
    fields = ['question','option1','option2','option3','option4','option1','rightop','userid']