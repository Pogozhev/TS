from django.db import models
from django.utils import timezone

# Create your models here.   models.ForeignKey -- ссылка на другую модель.
class Mail(models.Model):
    name = models.CharField(max_length=200)
    namber = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    created_date = models.DateTimeField(
        default=timezone.now)


    def publish(self): #def означает, что создаётся функция/метод (publish  <- this is metod name)
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title