from django.db import models
from django.utils.translation import gettext_lazy as _ 



class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ['id']

    
    def __str__(self):
        return self.name

class Quizzes(models.Model):
    category = models.ForeignKey(Category, default=1, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255, default=_('New Quiz'), verbose_name=_('Quiz Title'))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = _('Quiz')
        verbose_name_plural = _('Quizzes')
        ordering = ['id']

    def __str__(self):
        return self.title

class Updated(models.Model):
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Last Updated'))

    class Meta:
        abstract = True


class Questions(Updated):
    SCALE = (
        (0, _('Fundamental')),
        (1, _('Beginner')),
        (2, _('Intermediate')),
        (3, _('Advanced')),
        (4, _('Expert')),
    )
    TYPE = (
        (0, _('Multiple Choce')),
    )

    quiz = models.ForeignKey(Quizzes, related_name='question', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    technique = models.IntegerField(choices=TYPE, default=0, verbose_name='Type of Question')
    difficulty = models.IntegerField(choices=SCALE, default=0, verbose_name=_('Difficulty'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date Created'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Date Updated'))
    is_active = models.BooleanField(default=False, verbose_name=_('Active Status'))
    

    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')
        ordering = ['id']

    
    def __str__(self):
        return self.title



class Answer(Updated):
    question = models.ForeignKey(Questions, related_name='answer', on_delete=models.DO_NOTHING) 
    answer_text = models.CharField(max_length=200, verbose_name=_('Answer'))
    is_right = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Answer')
        verbose_name_plural = _('Answers')
        ordering = ['id']

    def __str__(self):
        return self.answer_text
    