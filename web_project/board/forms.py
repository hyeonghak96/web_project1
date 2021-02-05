from django import forms
from .models import Board, Comment

class BoardSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')
    target = forms.CharField(label='Search Target')

class CommentForm(forms.ModelForm):
    text = forms.TextInput(label = '댓글')

    class Meta:
        model = Comment
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].label = "댓글"