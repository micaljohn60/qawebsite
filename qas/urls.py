from django.urls import path,include
from qas import views


app_name = 'questions'

urlpatterns = [   
    path('questionslists/',views.index,name="questionlistis"),
    path('askquestion/',views.askquestion,name="askquestion"),
    path('<int:qids>/',views.question_detail,name="questiondetail"),
   
]