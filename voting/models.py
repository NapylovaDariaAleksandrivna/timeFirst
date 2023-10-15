from django.db import models

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=255)
    foto = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True, null=True, verbose_name="Фотография")
    nomination = models.CharField(max_length=255)
    id_condidate = models.CharField(primary_key=True, editable=False, max_length=10)
