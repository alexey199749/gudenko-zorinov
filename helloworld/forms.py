from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="Имя", localize="left")
    age = forms.IntegerField(label="Возраст")
    url = forms.URLField()
