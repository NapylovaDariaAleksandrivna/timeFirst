from django.contrib import admin

# Register your models here.
from .models import CandidateStudent,CandidateTeacher, N_ns

admin.site.register(CandidateStudent)
admin.site.register(CandidateTeacher)
admin.site.register(N_ns)