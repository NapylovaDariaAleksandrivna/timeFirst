from django.contrib import admin

# Register your models here.
from .models import CandidateStudent,CandidateTeacher, N_nsT, N_nsS, V, CandidateEvent,N_nsE

admin.site.register(CandidateStudent)
admin.site.register(CandidateTeacher)
admin.site.register(CandidateEvent)
admin.site.register(N_nsE)
admin.site.register(N_nsT)
admin.site.register(N_nsS)
admin.site.register(V)