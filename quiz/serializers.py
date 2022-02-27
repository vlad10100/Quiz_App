from rest_framework import serializers
from quiz.models import Quizzes, Questions, Answer


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quizzes
        fields = ['title', ]


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
    quiz = QuizSerializer(read_only=True)

    class Meta:
        model = Questions
        fields = ['quiz','title','answer'] # answer -->> related_name
