from django import forms

CITIES = (
    ('Juliaca', ("Juliaca")),
    ('Puno', ("Puno"))
)


class QueryForm(forms.Form):
    query = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={
            'class': 'mdl-textfield__input',
            'value': ' ',
            'required': 'required'
        }
    ))
    city = forms.CharField()
