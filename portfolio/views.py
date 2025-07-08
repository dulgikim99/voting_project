from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from .models import Project, Evaluation
from django.views.decorators.csrf import csrf_exempt

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/project_list.html', {
        'projects': projects,
    })

@csrf_exempt
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == "POST":
        user = request.POST.get("user", "익명")  
        score = int(request.POST.get("score"))
        Evaluation.objects.create(project=project, user=user, score=score)

        return redirect('project_detail', pk=pk)

    evaluations = project.evaluation_set.all()
    average = project.average_score()

    return render(request, 'portfolio/project_detail.html', {
        'project': project,
        'evaluations': evaluations,
        'average': average,
    })

def add_interest(request, pk):
    interests = request.session.get("interests", [])
    if pk not in interests:
        interests.append(pk)
        request.session["interests"] = interests
    return redirect('project_list')

def interest_list(request):
    interests = request.session.get("interests", [])
    projects = Project.objects.filter(pk__in=interests)
    return render(request, 'portfolio/interest_list.html', {'projects': projects})

def ranking_view(request):    #프로젝트별로 평균 점수를 구해 순위를 보여준다.
    projects = Project.objects.annotate(avg_score=Avg('evaluation__score')).order_by('-avg_score')
    return render(request, 'portfolio/ranking.html', {'projects': projects})


def evaluation_ranking(request):   #사용자가 내린 평가를 기준으로 점수 순위를 보여준다.(sorting)
    evaluations = Evaluation.objects.select_related('project').order_by('-score', 'evaluated_at')
    return render(request, 'portfolio/evaluation_ranking.html', {'evaluations': evaluations})
