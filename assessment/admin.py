# Register your models here.

from django.contrib import admin
from .models import Question, AnticipatedResponse, UserResponse

admin.site.register(Question)
admin.site.register(AnticipatedResponse)
admin.site.register(UserResponse)
