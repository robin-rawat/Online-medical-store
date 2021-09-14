from django import forms

class QueryInputForm(forms.Form):
    query_text = forms.CharField()