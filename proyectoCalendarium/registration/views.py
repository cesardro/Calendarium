from django.template import loader
from .forms import UsuarioCrearFormConEmail
from django.views.generic import CreateView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django import forms
from django.contrib.auth.views import LoginView

# Create your views here.
def login(request):
    return LoginView.as_view(template_name='registration/login.html')(request)

def vistasignup(request):
    home = loader.get_template('registration/SignUp.html')
    return HttpResponse(home.render())

class RegistroView(CreateView):
    form_class = UsuarioCrearFormConEmail
    
    template_name = 'registration/SignUp2.html'
    success_url = reverse_lazy('login')

    def get_success_url(self) -> str:
        return reverse_lazy('login')+'?registrado'
    
    
    def get_form(self, form_class=None):
        
        form = super(RegistroView,self).get_form()
        
        #modificamos los campos del formulario
        form.fields['email'].widget = forms.EmailInput(attrs={'placeholder':'Email'})
        form.fields['username'].widget = forms.TextInput(attrs={'placeholder':'Nombre'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder':'Repite la contraseña'})
        
        return form


    