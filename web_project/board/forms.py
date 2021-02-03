from django import forms
class BoardSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')
    target = forms.CharField(label='Search Target')