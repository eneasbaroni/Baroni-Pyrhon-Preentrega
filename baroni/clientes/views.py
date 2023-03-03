from django.shortcuts import render
from .models import Cliente
from .forms import ClienteForm

def list_clientes(request):
    
  all_clientes = Cliente.objects.all()
    
  context = {
    'clientes': all_clientes
  }
  
  return render(request, 'clientes/list_clientes.html', context)

def create_cliente(request):
  if request.method == 'GET':  
    form = ClienteForm()    
    return render(request, 'clientes/create_cliente.html', context={'form': form})
  else:
    form = ClienteForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      Cliente.objects.create(name = data['name'], last_name = data['last_name'], email = data['email'], phone = data['phone'], address = data['address'], credit = data['credit'], active = data['active'])
      return render(request, 'clientes/create_cliente.html', context={})
    else:
      context = {
        'form': form,
        'message': form.errors
      }
      return render(request, 'clientes/create_cliente.html', context)
      


