from django.db import models

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="media/skills/")

class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=1000)

    # def __str__(self):
    #     return self.email
