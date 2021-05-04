from django.contrib import admin

#veja a parte de models para criar esses models
from .models import Question
from .models import Choice

admin.site.register(Question)
admin.site.register(Choice)