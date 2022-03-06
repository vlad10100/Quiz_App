from rest_framework import serializers
from quiz.models import Quizzes, Questions, Answer, Category





class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']




class QuizSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Quizzes
        fields = ['title', 'category']




class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer 
        fields = ['id', 'answer_text', 'is_right']




class RandomQuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Questions
        fields = ['title', 'answer' ] # answer -->> related_name



class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Questions
        fields = ['title','answer'] # answer -->> related_name
