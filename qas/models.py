from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Questions(models.Model):
    title = models.CharField(max_length=800)
    detail = models.TextField()
    date = models.DateField(auto_now_add=True)    
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    
    def __str__(self):
        return self.title
    
class Solutions(models.Model):
    date = models.DateField(auto_now_add=True)
    solution = models.TextField()
    solve = models.BooleanField(default=False)
    qid = models.ForeignKey(Questions,on_delete=models.CASCADE,default=None)
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=None)   
    
    def __str__(self):
        return self.solution