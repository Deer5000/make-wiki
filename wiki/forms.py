from django import forms
from wiki.models import Article


class ArticleForm(forms.ModelForm):
    """ Render and process a form based on the Article model. """
    class Meta:
        fields = ['author','title', 'content']
        model = Article
