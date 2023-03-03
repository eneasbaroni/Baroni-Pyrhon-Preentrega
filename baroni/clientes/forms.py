from django import forms

class ClienteForm(forms.Form):    
    name = forms.CharField(label='Nombre', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nombre'})) 
    last_name = forms.CharField(label='Apellido', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))
    email = forms.EmailField(label='Email', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    phone = forms.CharField(label='Telefono', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Telefono'}))
    address = forms.CharField(label='Direccion', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Direccion'}))
    choicess = ( (True, 'Si'), (False, 'No') ) """ Opciones para poder armar booleano en el form """
    credit = forms.ChoiceField(label='Apto Credito', choices=choicess, widget=forms.RadioSelect)
    active = forms.ChoiceField(label='Activo', choices=choicess, widget=forms.RadioSelect)

