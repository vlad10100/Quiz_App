from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import HTMLFormRenderer


from quiz.serializers import QuizSerializer, RandomQuestionSerializer, QuestionSerializer, CategorySerializer
from quiz.models import Quizzes, Questions, Category, Answer


class QuizStart(APIView):
    # display all quiz categories
    def get(self, request, format=None):        
        category_list = Category.objects.all()
        serializer = CategorySerializer(category_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class Quiz(APIView):

    # display quizzes
    def get(self, request, format=None):
        quiz_list = Quizzes.objects.all()
        serializer = QuizSerializer(quiz_list, many=True)
        return Response(serializer.data)
    

    # create quiz title
    def post(self, request, format=None):
        serializer = QuizSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class RandomQuestion(APIView):
    def get(self, request, format=None, **kwargs):
        question = Questions.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1] # 1 RANDON at a time
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)


class QuestionList(APIView):
    
    def get(self, request, format=None, **kwargs):
        question = Questions.objects.filter(quiz__title=kwargs['topic'])                   # Display all questions
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)


class CreateQuiz(APIView):
    pass