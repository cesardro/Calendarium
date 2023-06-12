from django import forms

class TrackerForm(forms.Form):
    title = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Título'}),label=False)    
    options = (('', 'Seleccione tracker'),('To-do', 'To-do'),('Series', 'Series'),('Peliculas', 'Peliculas'),('Libros', 'Libros'))
    track_name = forms.ChoiceField(choices=options,label=False,widget=forms.Select(attrs={'class': 'form-select mt-3'}))
    
class EventoForm(forms.Form):
    title = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class': 'form-control'}), label="Título")
    description = forms.CharField(max_length=255,widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),label="Descripción")
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),label="Fecha")
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}), label="Hora")

class TareaForm(forms.Form):
    title = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class': 'form-control'}), label="Título")
    description = forms.CharField(max_length=255,widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),label="Descripción")
    exp_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),label="Fecha")
    options = (('', 'Selecciona una prioridad'),('Urgente', 'Urgente'),('Importante', 'Importante'),('No importante', 'No importante'))
    priority = forms.ChoiceField(choices=options,label=False,widget=forms.Select(attrs={'class': 'form-select'}))

class CumpleanoForm(forms.Form):
    name = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class': 'form-control'}), label="Cumpleañero")
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),label="Fecha")
