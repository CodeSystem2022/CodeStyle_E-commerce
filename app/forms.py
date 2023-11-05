from django import forms
from django.contrib.auth.forms import (
    UserCreationForm, AuthenticationForm, UsernameField, 
    PasswordChangeForm, SetPasswordForm, PasswordResetForm
)
from django.contrib.auth.models import User
from . models import Customer

# Formulario de inicio de sesión
class LoginForm(AuthenticationForm):
    username = UsernameField(label='Usuario',widget=forms.TextInput(attrs={'autofocus':'True','class': 'form-control'}))
    password = forms.CharField(label='Contraseña',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

# Formulario de registrarse
class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Usuario',widget=forms.TextInput(attrs={'autofocus':'True','class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Formulario de cambio de contraseña 
class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Contraseña anterior', widget=forms.PasswordInput(attrs={'autofocus':'True','autocomplete':'current-password','class':'form-control'}))
    new_password1 = forms.CharField(label='Nueva contraseña', widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))      
    new_password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))   

# Formulario de restablecimiento de contraseña personalizado
class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

# Formulario de configuración de nueva contraseña personalizado
class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='Nueva contraseña', widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))      
    new_password2 = forms.CharField(label='Confirme nueva contraseña', widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))  

# Formulario de perfil de usuario
class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'locality', 'city', 'mobile', 'state', 'zipcode']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'zipcode': forms.NumberInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'name': 'Nombre',
            'locality': 'Dirección',
            'city': 'Ciudad',
            'mobile': 'Celular',
            'state': 'Provincia',
            'zipcode': 'Código postal',
        }

        state = forms.CharField(
        max_length=9,  # Limita la entrada a 5 caracteres
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        )
