from django.urls import path 
from quiz.views import Quiz, RandomQuestion, QuestionList, QuizStart

app_name = 'quiz'

urlpatterns = [
    path('', QuizStart.as_view(), name='starting-point'),
    path('quiz/', Quiz.as_view(), name='quiz'),
    path('r/<str:topic>/', RandomQuestion.as_view(), name='question'),
    path('q/<str:topic>/', QuestionList.as_view(), name='quiz-question'),
]