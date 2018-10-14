from django import forms


class UserForm(forms.Form):
    id = forms.IntegerField(required=False, min_value=1)
    process = forms.CharField(max_length=20)
    user = forms.CharField(required=False)
