from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsuarioCrearFormConEmail(UserCreationForm):
    email = forms.EmailField(required=True,help_text="Obligatorio un e-mail válido.",label=False)
    username = forms.CharField(required=True,help_text="Elige un nombre de usuario valido.",label=False)
    password1 = forms.CharField(required=True,help_text="Tiene que contener letra mayuscula, un numero y un caracter especial, minimo 8 caracteres en total",label=False)
    password2 = forms.CharField(required=True,help_text="",label=False)

    class Meta:
        model = User
        fields = ("email","username","password1","password2")
        
    def clean_email(self):
        correo = self.cleaned_data.get("email")
        
        #comprobar que el email no exite
        if User.objects.filter(email=correo).exists():
            raise forms.ValidationError("Error: Ya hay un Usuario con este correo")
        
        return correo