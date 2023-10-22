from django.db import models
import uuid
# Create your models here.
class CandidateTeacher(models.Model):
    class N_ns(models.TextChoices):
        n1="Самый стильный преподаватель",'Самый стильный преподаватель'
        n2="Самый прогрессивный преподаватель",'Самый прогрессивный преподаватель'
        n3="Лучший лектор",'Лучший лектор'
        n4="Лучший наставник",'Лучший наставник'
        n5="Преподаватель года",'Преподаватель года'
        
    nominations=models.CharField(max_length=255,choices=N_ns.choices)
    name = models.CharField(max_length=255)
    foto = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True, null=True, verbose_name="Фотография")
    department = models.CharField(max_length=255)
    experience = models.IntegerField()
    about=models.TextField()
    id_T = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    def __str__(self):
        return self.nominations+" - "+self.name

class CandidateStudent(models.Model):
    class N_ns(models.TextChoices):
        n1="Активист года",'Активист года'
        n2="Спортсмен года",'Спортсмен года'
        n3="Изобретатель года",'Изобретатель года'
        n4="Политехник года",'Политехник года'
        n5="Видео",'Видео'
        n6="Дизайн",'Дизайн'
        n7="Фото",'Фото'
        
    nominations=models.CharField(max_length=255,choices=N_ns.choices)
    name = models.CharField(max_length=255)
    foto = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True, null=True, verbose_name="Фотография")
    institute = models.CharField(max_length=25)
    group = models.CharField(max_length=25)
    about=models.TextField()
    id_S = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    def __str__(self):
        return self.nominations+" - "+self.name