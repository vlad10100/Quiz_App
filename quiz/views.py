from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView


from quiz.serializers import QuizSerializer, RandomQuestionSerializer, QuestionSerializer
from quiz.models import Quizzes, Questions

class Quiz(generics.ListAPIView):
    queryset = Quizzes.objects.all()
    serializer_class = QuizSerializer


class RandomQuestion(APIView):
    
    def get(self, request, format=None, **kwargs):
        question = Questions.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)


class QuizQuestion(APIView):
    
    def get(self, request, format=None, **kwargs):
        question = Questions.objects.filter(quiz__title=kwargs['topic'])
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)