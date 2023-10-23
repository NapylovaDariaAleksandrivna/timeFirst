from django.db import models
import uuid
# Create your models here.
class N_ns(models.Model):
    class N_nsС(models.TextChoices):
        n1="Самый стильный преподаватель",'Самый стильный преподаватель'
        n2="Самый прогрессивный преподаватель",'Самый прогрессивный преподаватель'
        n3="Лучший лектор",'Лучший лектор'
        n4="Лучший наставник",'Лучший наставник'
        n5="Преподаватель года",'Преподаватель года'
        n6="Активист года",'Активист года'
        n7="Спортсмен года",'Спортсмен года'
        n8="Изобретатель года",'Изобретатель года'
        n9="Политехник года",'Политехник года'
        n10="Видео",'Видео'
        n11="Дизайн",'Дизайн'
        n12="Фото",'Фото'
    name=models.CharField(max_length=255,choices=N_nsС.choices)
    def __str__(self):
        return self.name
    class Meta:
        db_table = "Номинации"

class CandidateTeacher(models.Model):
    nominations=models.ForeignKey(N_ns, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    foto = models.ImageField(upload_to="Teachers/", blank=True, null=True, verbose_name="Фотография")
    department = models.CharField(max_length=255)
    experience = models.IntegerField()
    about=models.TextField()
    id_T = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    def __str__(self):
        return self.nominations.name+" - "+self.name
    class Meta:
        db_table = "Преподаватели"


class CandidateStudent(models.Model):
    nominations=models.ForeignKey('N_ns', on_delete=models.CASCADE, related_name='nominationss')
    name = models.CharField(max_length=255)
    foto = models.ImageField(upload_to="Students/", blank=True, null=True)
    institute = models.CharField(max_length=25)
    group = models.CharField(max_length=25)
    about=models.TextField()
    id_S = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    def __str__(self):
        return self.nominations.name+" - "+self.name
    class Meta:
        db_table = "Студенты"