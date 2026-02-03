from django import forms

class CitySelectForm(forms.Form):
    city = forms.ChoiceField(choices=[])  # keuzes vullen we later dynamisch

    def __init__(self, *args, **kwargs):
        cities = kwargs.pop('cities', [])
        super().__init__(*args, **kwargs)
        # keuzes vullen zoals in je huidige HTML
        self.fields['city'].choices = [(city.code, city.name) for city in cities]
