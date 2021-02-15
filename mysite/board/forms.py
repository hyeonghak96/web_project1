from django import forms
from .models import Board, Comment   #, Question, Answer

class BoardForm(forms.Form):
    title = forms.CharField(label = "제목")
    description = forms.CharField(label = "간단 설명")
    content = forms.CharField(label = "내용")
    tags = forms.CharField(label = "Tags")

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