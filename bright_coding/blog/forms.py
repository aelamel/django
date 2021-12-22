from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Article

#fields = "__all__"

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        # fields = ["title", "description", "category", "tags"]
        exclude = ["state"]

        widgets ={
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }