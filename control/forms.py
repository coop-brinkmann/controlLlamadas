from django import forms


class LamaForm(forms.Form):
    lama = forms.FileField()

class AmaForm(forms.Form):
    ama = forms.FileField()