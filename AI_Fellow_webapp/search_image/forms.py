from django import forms

class image_input(forms.Form):
    image_input = forms.CharField(label='image_input', max_length=100)