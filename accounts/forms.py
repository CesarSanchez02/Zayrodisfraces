from django import forms
from django.forms import DateInput
from allauth.account.forms import SignupForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email", "fecha_nacimiento", "direccion", "telefono")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email", "fecha_nacimiento", "direccion", "telefono")

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='Nombres:', required=True, 
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tus nombres'}))
    last_name = forms.CharField(max_length=30, label='Apellidos:', required=True, 
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tus apellidos'}))
    email = forms.EmailField(max_length=254, label='Correo electrónico:', required=True,
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}))
    password1 = forms.CharField(label='Contraseña:', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
    password2 = forms.CharField(label='Contraseña (de nuevo):', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña (de nuevo)'}))
    
    fecha_nacimiento = forms.DateField(label='Fecha nacimiento:', 
                                        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), 
                                        required=True)
    direccion = forms.CharField(max_length=255, label='Dirección:', required=True, 
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su dirección'}))
    telefono = forms.CharField(max_length=255, label='Teléfono:', required=False, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su número'}))

    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.fecha_nacimiento = self.cleaned_data['fecha_nacimiento']
        user.direccion = self.cleaned_data['direccion']
        user.telefono = self.cleaned_data['telefono']
        user.save()
        return user