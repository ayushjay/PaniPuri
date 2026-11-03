from django.db import models
from django.core.validators import MinLengthValidator

class UserInputModel(models.Model):
    prayer = models.CharField(max_length=300)
    user_prompt = models.CharField(max_length=300,validators=[MinLengthValidator(2)])

    def __str__(self):
        return self.title

