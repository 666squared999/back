from django.db import models
from django.contrib.postgres.fields import ArrayField

SEX_CHOICES = [
    ('woman', 'woman'),
    ('man', 'man'),
]

class Advert(models.Model):
    title = models.CharField(max_length=30)
    photo_urls = ArrayField(models.CharField(max_length=200), size=5)
    animal_type = models.CharField(max_length=15)
    breed = models.CharField(max_length=30)
    color = models.CharField(max_length=15)
    sex = models.CharField(
        max_length=max(len(el[0]) for el in SEX_CHOICES),
        choices=SEX_CHOICES
    )
    description = models.CharField(max_length=600)