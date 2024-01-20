from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    text_color = models.CharField(max_length=7)
    background_color = models.CharField(max_length=7)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=255, blank=False, validators=[MinLengthValidator(2)])
    description = models.TextField(validators=[MinLengthValidator(2)], blank=False)
    image = models.URLField()
    publish_date = models.DateTimeField(blank=False)
    categories = models.ManyToManyField(Category)
    author = models.CharField(max_length=255, blank=False, validators=[MinLengthValidator(4)])
    email = models.EmailField(blank=True, null=True)


    def __str__(self):
        return self.title
