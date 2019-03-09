from django.shortcuts import render
from django.contrib.auth.models import
from django.views.generic import CreateView,ListView,UpdateView,FormView
from .models import Questions
from .form import LoginForm

# Create your views here.


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'auth/login.html'

    # def form_valid(self, form):
    #     auth_login(self.request, form.get_user())


class AddQuestion(CreateView):
    model = Questions
    fields = ['question','option1','option2','option3','option4','option1','rightop']

class ListQuestion(ListView):
    model = Questions
    template_name = 'onlinequiz/list.html'

class EditQuestions(UpdateView):
    model = Questions
    fields = ['question', 'option1', 'option2', 'option3', 'option4', 'option1', 'rightop']

