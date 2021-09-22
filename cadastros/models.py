from django.db import models

# Create your models here.

class Campo(models.Model):
    email = models.CharField(max_length=50)
    senha = models.CharField(max_length=20)

    def __str__(self):
        return "{} ({})".format(self.email, self.senha)