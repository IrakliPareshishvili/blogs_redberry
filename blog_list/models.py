from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    text_color = models.CharField(max_length=7)
    background_color = models.CharField(max_length=7)

class Blog(models.Model):
    title = models.CharField(max_length=255, blank=False, validators=[MinLengthValidator(2)])
    description = models.TextField(validators=[MinLengthValidator(2)], blank=False)
    image = models.URLField()
    publish_date = models.DateTimeField(blank=False)
    categories = models.ManyToManyField(Category)
    author = models.CharField(max_length=255, blank=False, validators=[MinLengthValidator(4)])
    email = models.EmailField(blank=True, null=True)

    def clean(self):
        if not any(char.isalpha() for char in self.author):
            raise ValidationError("Author must contain at least one letter.")
        words = self.author.split()
        if len(words) < 2:
            raise ValidationError("Author must have at least two words.")

    def __str__(self):
        return self.title
