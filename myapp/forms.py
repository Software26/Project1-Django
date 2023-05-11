from django import forms

class CreateNewTask(forms.Form):
    title = forms.Charfield(label="Tutulo de tarea", max_length = 200)
    description = forms.Textarea(with)