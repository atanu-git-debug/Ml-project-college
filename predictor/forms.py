from django import forms

class PredictionForm(forms.Form):
    age = forms.FloatField(
        label="Age",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    salary = forms.FloatField(
        label="Estimated Salary",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )