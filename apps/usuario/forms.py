from django import forms

#creacion formularios
class FormularioLogin(forms.Form):
    username = forms.CharField(label="Usuario", widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Ingrese su usuario'}))
    password = forms.CharField(label="Clave", widget = forms.PasswordInput(
        attrs={'class':'form-control', 'placeholder':'Ingrese su clave'}))