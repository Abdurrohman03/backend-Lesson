import random
import string

from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save


class Article(models.Model):
    title = models.CharField(max_length=225)
    content = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    image = models.ImageField(upload_to='articles', null=True, blank=True, help_text='2 mbdan oshmasin')
    modified_date = models.DateTimeField(auto_now=True, null=True)
    created_data = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    # def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
    #     if self.slug is None:
    #         self.slug = slugify(self.title)
    #     try:
    #         super().save()
    #     except Exception as e:
    #         rand = "".join(random.choice(string.ascii_lowercase) for _ in range(4))
    #         self.slug = slugify(self.title) + f"-{rand}"
    #         super().save()



