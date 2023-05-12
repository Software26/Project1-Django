from django import forms

class CreateNewTask(forms.Form):
    
    title = forms.CharField(label="Tutulo de tarea", max_length = 200)
    
    description = forms.CharField(label = "Descripcion de la tarea", widget=forms.Textarea)