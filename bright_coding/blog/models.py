from typing import Text
from django.db import models
from django.db.models.fields import BooleanField, CharField, DateTimeField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey, ManyToManyField

# Create your models here.
AVAILABLE_STATE = (
        (0, 'Disabled'),
        (1, 'Enabled')
    )
class Category(models.Model):
    name = CharField(max_length=50)
    state = IntegerField(default=0, choices=AVAILABLE_STATE)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Article (models.Model):
    title = CharField(max_length=120, null=True, unique=True)
    description = TextField(null=True, blank=True)
    category = ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    tags = ManyToManyField("Tag")
    state = IntegerField(default=0, choices=AVAILABLE_STATE)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class Tag(models.Model):
    name = CharField(max_length=20)
    #articles = ManyToManyField("Article")
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
