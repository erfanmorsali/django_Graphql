from django.db import models
from django.utils.text import slugify
from category.models import Category


# Create your models here.


class Post(models.Model):
    slug = models.SlugField(unique=True, db_index=True, allow_unicode=True, null=True, blank=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True,blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
