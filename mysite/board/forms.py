from django import forms
from .models import Board, Comment   #, Question, Answer

class BoardSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')
    target = forms.CharField(label='Search Target')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
        labels = {
            'text': '댓글내용',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].label = "댓글"