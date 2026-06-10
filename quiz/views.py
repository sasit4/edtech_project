
from django.shortcuts import render, redirect
from .models import Quiz, Question, Result

def quiz_page(request, id):

    quiz = Quiz.objects.get(id=id)
    questions = Question.objects.filter(quiz=quiz)

    if request.method == "POST":

        score = 0

        for q in questions:
            answer = request.POST.get(str(q.id))
            if answer == q.correct_answer:
                score += 1

        Result.objects.create(
            user=request.user,
            quiz=quiz,
            score=score
        )

        return redirect('quiz_result', id=quiz.id)

    return render(request, 'quiz/quiz.html', {
        'quiz': quiz,
        'questions': questions
    })


def quiz_result(request, id):

    quiz = Quiz.objects.get(id=id)

    result = Result.objects.filter(
        user=request.user,
        quiz=quiz
    ).last()

    return render(request, 'quiz/result.html', {
        'result': result
    })


def leaderboard(request):

    leaders = Result.objects.order_by('-score')[:5]

    return render(request, 'quiz/leaderboard.html', {
        'leaders': leaders

    })