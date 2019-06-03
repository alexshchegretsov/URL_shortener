from django import forms


class UrlForm(forms.Form):
    url = forms.URLField(
        label=False,
        widget=forms.TextInput(attrs={"placeholder": "http://google.com"})
    )
