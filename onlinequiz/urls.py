from django.urls import path,include
from .views import AddQuestion

urlpatterns = [

    path('add/',AddQuestion.as_view(),name = "addquestion"),

   # path('login/',)
]