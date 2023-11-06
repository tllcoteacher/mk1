# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# Validator for the standard field format
standard_format_validator = RegexValidator(
    regex=r'^\d+(\.\w+){2}$',
    message="Standard must be in the format of 'x.xx.x' or 'x.xxx.x' where x is a number"
)

class Question(models.Model):
    GRADE_CHOICES = (
        ('PK', 'Pre-Kindergarten'),
        ('K', 'Kindergarten'),
    ) + tuple((str(k), f"Grade {k}") for k in range(1, 7))

    grade = models.CharField(
        max_length=2,
        choices=GRADE_CHOICES,
        blank=True,
        null=True
    )
    text = models.TextField()
    image = models.ImageField(upload_to='questions/', blank=True, null=True)
    level_of_understanding = models.PositiveSmallIntegerField(blank=True, null=True)
    standard = models.CharField(
        max_length=10, 
        validators=[standard_format_validator], 
        blank=True, 
        null=True
    )

    def __str__(self):
        return self.text
        
class AnticipatedResponse(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    level_of_understanding = models.PositiveSmallIntegerField()
    standard = models.CharField(
        max_length=10, 
        validators=[standard_format_validator], 
        blank=True, 
        null=True
    )

    def __str__(self):
        return self.text
        
class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    level_of_understanding = models.PositiveSmallIntegerField(blank=True, null=True)
    standard = models.CharField(
        max_length=10, 
        validators=[standard_format_validator], 
        blank=True, 
        null=True
    )

    def __str__(self):
        return self.text