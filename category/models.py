from django.db import models
from django.utils.text import slugify


# Create your models here.


class Category(models.Model):
    slug = models.SlugField(allow_unicode=True, unique=True, db_index=True, null=True, blank=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

