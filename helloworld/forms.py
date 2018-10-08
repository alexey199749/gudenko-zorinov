from django import forms


class UserForm(forms.Form):
    process = forms.CharField(max_length=10)
    ID = forms.IntegerField(required=False, min_value=1)
    user = forms.CharField(required=False)
