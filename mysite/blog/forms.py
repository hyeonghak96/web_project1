from django import forms

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label = 'Search Word') # 여긴 필수항목이라고 나옴
    #target = forms.CharField(label = 'Search Target')