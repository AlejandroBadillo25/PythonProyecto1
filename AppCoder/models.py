from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    class Estado(models.TextChoices):
        BORRADOR = "B", "Borrador"
        PUBLICADO = "P", "Publicado"
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.CharField(
        max_length=1,
        choices=Estado.choices,
        default=Estado.BORRADOR,
    )

    def __str__(self):
        return self.title
