from django.contrib.postgres.fields import ArrayField
from django_s3_storage.storage import S3Storage
from django.conf import settings
from django.db import models

storage = S3Storage(aws_s3_bucket_name=settings.AWS_STORAGE_BUCKET_NAME)

SEX_CHOICES = [
    ('woman', 'woman'),
    ('man', 'man'),
]

class Advert(models.Model):
    title = models.CharField(max_length=30)
    photo_urls = models.ImageField(storage=storage, null=True)
    animal_type = models.CharField(max_length=15)
    breed = models.CharField(max_length=30)
    color = models.CharField(max_length=15)
    sex = models.CharField(
        max_length=max(len(el[0]) for el in SEX_CHOICES),
        choices=SEX_CHOICES
    )
    description = models.CharField(max_length=600)