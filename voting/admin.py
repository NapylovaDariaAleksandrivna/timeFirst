from django.contrib import admin

# Register your models here.
from .models import CandidateStudent,CandidateTeacher

admin.site.register(CandidateStudent)
admin.site.register(CandidateTeacher)