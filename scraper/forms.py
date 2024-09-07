from django import forms

class KeywordForm(forms.Form):
    keyword = forms.CharField(label='Enter Keyword', max_length=100)
