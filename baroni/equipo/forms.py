from django import forms

class MemberForm(forms.Form):    
  name = forms.CharField(label='Nombre', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nombre'})) 
  last_name = forms.CharField(label='Apellido', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))
  email = forms.EmailField(label='Email', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
  phone = forms.CharField(label='Telefono', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Telefono'}))
  bio = forms.CharField(label='Biografia', max_length=400, widget=forms.TextInput(attrs={'placeholder': 'Biografía'}))
  position = forms.CharField(label='Cargo', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Cargo'}))
  image = forms.FileField(label='Imagen', required=True)