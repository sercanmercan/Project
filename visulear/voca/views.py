'''
Created on 10 May 2018

@author: Sercan
'''
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from . import models

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def vocab(request, tSid):
    # 기존에 문제를 풀었는지 체크하여
    ExistAnswer = models.UserAnswer.objects.filter(user = request.user, question__part__testSet__pk=tSid)
    # 기존에 문제를 푼 경험이 있으면 결과화면으로 redirect
    if len(ExistAnswer) > 0:
        return HttpResponseRedirect('/result/' + str(tSid) + '/')

    # 문제셋에 포함된 파트 불러오기
    Parts = models.Part.objects.filter(testSet = tSid)

    Questions = []

    # 각 파트별로
    for Part in Parts:
        PartItem = {}
        PartItem['title'] = Part.title # 파트명 불러오기
        PartItem['questions'] = models.Question.objects.filter(part = Part) # 파트에 속해있는 문제 불러오기
        Questions.append(PartItem)
    # Parts라는 이름으로 전체 질문 한번에 보내기
    return render(request, 'vocab_part.html', {'Parts':Questions})


# 각 질문에 대한 답변이 저장될 때 마다 호출되는 AJAX용 뷰
@login_required
def saveVocab(request, qid):
    try:
        question = models.Question.objects.get(pk = qid)
        newAnswer = models.UserAnswer(
            user = request.user, 
            question = question, 
            answer = request.POST['answer'], 
            is_correct = int(request.POST['answer']) == question.answer # 문제의 정답과 사용자 답변이 같으면 true
        )

        # 저장까지 완료되면 success를 리턴
        newAnswer.save()
        return HttpResponse('success')
    except:
        return HttpResponse('fail')

@login_required
def result(request, tSid):
    # 특정 테스트셋에 대한 유저의 전체 답변을 파트 번호 순으로 정렬해서 가져온다.
    allAnswer = models.UserAnswer.objects.filter(user = request.user, question__part__testSet__pk=tSid).order_by('question__part__pk')

    # 답변내용이 없으면 질답화면으로 redirect
    if len(allAnswer) == 0:
        return HttpResponseRedirect('/vocab_part/' + str(tSid) + '/')

    # 파트별로 점수를 계산하기 위해 배열에 파트별 총 답변 개수와 정답 개수를 저장한다.
    scoreIndex = {}
    scores = []
    total = []

    for answer in allAnswer:
        try:
            total[scoreIndex[answer.question.part.pk]] = total[scoreIndex[answer.question.part.pk]] + 1
            if answer.is_correct:
                scores[scoreIndex[answer.question.part.pk]] = scores[scoreIndex[answer.question.part.pk]] + 1
        except:
            if answer.is_correct:
                scores.append(1)
            else:
                scores.append(0)
            total.append(1)
            scoreIndex[answer.question.part.pk] = len(scores) - 1

    # 파트별로 정답 개수를 답변 개수로 나눈 후 100을 곱하여 100점 만점으로 점수를 계산한다.
    for index in range(0, len(total)):
        scores[index] = int(scores[index] / total[index] * 100)

    return render(request, 'result.html', {'scores':scores})