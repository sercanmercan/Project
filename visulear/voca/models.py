from django.db import models
from django.contrib.auth.models import User

class TestSet(models.Model):
    title = models.CharField('문제세트명',max_length=256)
    
    def __str__(self):
        return self.title

class Part(models.Model):
    testSet = models.ForeignKey(TestSet, on_delete=models.CASCADE)
    title = models.CharField('파트안내',max_length=256)
    
    def __str__(self):
        return self.title

class Question(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    question = models.CharField('질문', max_length=256)
    image = models.FileField('이미지', upload_to='images', null=True, blank=True)
    choice1 = models.CharField('보기1', max_length=512)
    choice2 = models.CharField('보기2', max_length=512)
    choice3 = models.CharField('보기3', max_length=512)
    answer = models.IntegerField('정답')

    def __str__(self):
        return self.part.title + ' : ' +self.question

class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.IntegerField('답변')
    is_correct = models.BooleanField(default = False)

    def __str__(self):
        return self.user.username + ' : ' + self.question.part.title + ' : ' + self.question.question + ' : ' + str(self.is_correct)

class UserScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    score = models.IntegerField()