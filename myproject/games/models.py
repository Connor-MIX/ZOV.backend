from django.db import models

# Create your models here.
class Game(models.Model):
    title = models.CharField("Название", max_length=50)
    description = models.TextField("Описание")
    author = models.CharField("Автор статьи", max_length=20) # Временно
    platform = models.CharField("Платформа", max_length=20)
    created_at = models.DateTimeField("Дата создания ", auto_now_add=True)
    updated_at = models.DateTimeField("Дата последнего изменения", auto_now=True)

    def __str__(self):
        return self.title