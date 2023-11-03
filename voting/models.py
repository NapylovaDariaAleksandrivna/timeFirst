from django.db import models
import uuid
# Create your models here.
class N_nsT(models.Model):
    class N_nsС(models.TextChoices):
        n1="Самый стильный",'Самый стильный'
        n2="Самый прогрессивный",'Самый прогрессивный'
        n3="Лучший лектор",'Лучший лектор'
        n4="Наставник года",'Наставник года'
        n5="Преподаватель года",'Преподаватель года'
    name=models.CharField(max_length=255,choices=N_nsС.choices, unique=True)
    def __str__(self):
        return self.name
class N_nsS(models.Model):
    class N_nsС(models.TextChoices):
        n6="Активист года",'Активист года'
        n7="Спортсмен года",'Спортсмен года'
        n8="Изобретатель года",'Изобретатель года'
        n9="Политехник года",'Политехник года'
        n10="Техническое искусство. Видео",'Техническое искусство. Видео'
        n11="Техническое искусство. Дизайн",'Техническое искусство. Дизайн'
        n12="Техническое искусство. Фото",'Техническое искусство. Фото'
    name=models.CharField(max_length=255,choices=N_nsС.choices, unique=True)
    def __str__(self):
        return self.name
class N_nsE(models.Model):
    class N_nsС(models.TextChoices):
        n13="Мероприятие года",'Мероприятие года'
    name=models.CharField(max_length=255,choices=N_nsС.choices, unique=True, default="Мероприятие года")
    def __str__(self):
        return self.name
    

class CandidateEvent(models.Model):
    nominations=models.ForeignKey(N_nsE, on_delete=models.CASCADE)
    first_name= models.CharField(max_length=255, default="123")
    second_name=""
    foto = models.ImageField(upload_to="Event/", blank=True, verbose_name="Фотография", default='default.jpg')
    organizers = models.CharField(max_length=255)
    id_E = models.AutoField(primary_key=True)
    about=models.TextField()
    def __str__(self):
        return self.nominations.name+" - "+self.first_name
    class Meta:
        db_table = "Мероприятия"


class CandidateTeacher(models.Model):
    nominations=models.ForeignKey(N_nsT, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, default="123")
    second_name= models.CharField(max_length=255, default="123")
    foto = models.ImageField(upload_to="Teachers/", blank=True, verbose_name="Фотография", default='default.jpg')
    department = models.CharField(max_length=255)
    experience = models.IntegerField()
    about=models.TextField()
    id_T = models.AutoField(primary_key=True)
    def __str__(self):
        return self.nominations.name+" - "+self.first_name+" "+self.second_name
    class Meta:
        db_table = "Преподаватели"


class CandidateStudent(models.Model):
    nominations=models.ForeignKey(N_nsS, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, default="123")
    second_name= models.CharField(max_length=255, default="123")
    foto = models.ImageField(upload_to="Students/", blank=True, default='default.jpg')
    institute = models.CharField(max_length=25)
    group = models.CharField(max_length=25)
    about=models.TextField()
    id_S = models.AutoField(primary_key=True)
    def __str__(self):
        return self.nominations.name+" - "+self.first_name+" "+self.second_name
    class Meta:
        db_table = "Студенты"

class V(models.Model):
    nomination1=models.ForeignKey(CandidateTeacher, on_delete=models.CASCADE,related_name='vn1')
    nomination2=models.ForeignKey(CandidateTeacher, on_delete=models.CASCADE,related_name='vn2')
    nomination3=models.ForeignKey(CandidateTeacher, on_delete=models.CASCADE,related_name='vn3')
    nomination4=models.ForeignKey(CandidateTeacher, on_delete=models.CASCADE,related_name='vn4')
    nomination5=models.ForeignKey(CandidateTeacher, on_delete=models.CASCADE,related_name='vn5')

    nomination6=models.ForeignKey(CandidateStudent, on_delete=models.CASCADE,related_name='vn6')
    nomination7=models.ForeignKey(CandidateStudent, on_delete=models.CASCADE,related_name='vn7')
    nomination8=models.ForeignKey(CandidateStudent, on_delete=models.CASCADE,related_name='vn8')
    nomination9=models.ForeignKey(CandidateStudent, on_delete=models.CASCADE,related_name='vn9')
    nomination10=models.ForeignKey(CandidateStudent, on_delete=models.CASCADE,related_name='vn10')
    nomination11=models.ForeignKey(CandidateStudent, on_delete=models.CASCADE,related_name='vn11')
    nomination12=models.ForeignKey(CandidateStudent, on_delete=models.CASCADE,related_name='vn12')

    nomination13=models.ForeignKey(CandidateEvent, on_delete=models.CASCADE,related_name='vn13')