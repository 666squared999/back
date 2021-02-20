from django.contrib.postgres.fields import ArrayField
from django_s3_storage.storage import S3Storage
from users.models import User
from django.conf import settings
from django.db import models

storage = S3Storage(aws_s3_bucket_name=settings.AWS_STORAGE_BUCKET_NAME)

SEX_CHOICES = [
    ('woman', 'woman'),
    ('man', 'man'),
]

class Advert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='adverts')
    title = models.CharField(max_length=30)
    photo_urls = ArrayField(models.ImageField(storage=storage, null=True), default=list)
    animal_type = models.CharField(max_length=15, blank=True, null=True)
    breed = models.CharField(max_length=30, blank=True, null=True)
    color = models.CharField(max_length=15, blank=True, null=True)
    sex = models.CharField(
        max_length=max(len(el[0]) for el in SEX_CHOICES),
        choices=SEX_CHOICES,
        default="man",
        blank=True,
        null=True,
    )
    description = models.CharField(max_length=600, blank=True, null=True)
    animal_features = models.JSONField(blank=True, default=dict)
