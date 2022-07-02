from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
# Create your models here.
class LinksApp(models.Model):
    


    target_url = models.URLField(max_length=200)
    description = models.Charfield(max_length=200)
    slug = models.SlugField(max_length=20, blank=True, unique=True)
    author = models.ForeignKey(
        get_user_model()
    )
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)