from django.db import models

# Create your models here.
class Candidate(models.Model):
    class N_ns(models.TextChoices):
        n1="n1",'Самый стильный преподаватель'
        n2="n2",'Самый инновационный преподаватель'
        n3="n3",'Лучший лектор'
        n4="n4",'Душа компании'
        n5="n5",'Активист года'
        n6="n6",'Самый изобретательный'
        n7="n7",'Спортсмен года'
        n8="n8",'Самый творческий'
        n9="n9",'ПОЛИТЕХНИК ГОДА'
        n10="n10",'ПРЕПОДАВАТЕЛЯ ГОДА'
        n11="n11",'Мероприятие года'
        
    
    nominations=models.CharField(max_length=255,choices=N_ns.choices)
    name = models.CharField(max_length=255)
    foto = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True, null=True, verbose_name="Фотография")
    id_condidate = models.CharField(primary_key=True, editable=False, max_length=10)
