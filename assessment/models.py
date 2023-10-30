# Create your models here.

from django.db import models
from django.contrib.auth.models import User
        
class Question(models.Model):
    grade = models.PositiveSmallIntegerField(choices=[(k, f"Grade {k}") for k in range(1, 7)], blank=True, null=True)
    text = models.TextField()
    image = models.ImageField(upload_to='questions/', blank=True, null=True)
    level = models.PositiveSmallIntegerField(blank=True, null=True)
            
    def __str__(self):
        return self.text
        
class AnticipatedResponse(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    level = models.PositiveSmallIntegerField()
            
    def __str__(self):
        return self.text
        
class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    level = models.PositiveSmallIntegerField(blank=True, null=True)
            
    def __str__(self):
        return self.text