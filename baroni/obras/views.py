from django.shortcuts import render
from .models import Obra
from .forms import ObraForm

def list_obras(request):
  """ if search """
  if 'search' in request.GET:
    all_obras = Obra.objects.filter(name__icontains = request.GET.get('search'))
  else:
    all_obras = Obra.objects.all()
    
  context = {
    'obras': all_obras
  }
  return render(request, 'obras/list_obras.html', context)

def obra_detail(request, id):
  obra = Obra.objects.get(id = id)
  context = {
    'obra': obra
  }
  return render(request, 'obras/obra_detail.html', context)

""" def create_obra(request):
  if request.method == 'GET':      
    return render(request, 'obras/create_obra.html', context={})
  else:
    name = request.POST.get('name')
    price = request.POST.get('price')
    area = request.POST.get('area')
    description = request.POST.get('description')
    credit = request.POST.get('credit')
    image = request.FILES.get('image')
    Obra.objects.create(name = name, price = price, area = area, description = description, credit = credit, image = image)
    return render(request, 'obras/create_obra.html', context={}) """

def create_obra(request):
  if request.method == 'GET':  
    form = ObraForm()    
    return render(request, 'obras/create_obra.html', context={'form': form})
  else:
    form = ObraForm(request.POST, request.FILES)
    if form.is_valid():
      data = form.cleaned_data
      Obra.objects.create(name = data['name'], price = data['price'], area = data['area'], description = data['description'], credit = data['credit'], image = data['image'])
      return render(request, 'obras/create_obra.html', context={})
    else:
      context = {
        'form': form,
        'message': form.errors
      }
      return render(request, 'obras/create_obra.html', context)

    

   
    



# Create your views here.
