from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def average_score(self):
        evaluations = self.evaluation_set.all()
        if evaluations:
            return round(sum(e.score for e in evaluations) / evaluations.count(), 2)
        return None


class Evaluation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)  
    score = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    evaluated_at = models.DateTimeField(auto_now_add=True)

