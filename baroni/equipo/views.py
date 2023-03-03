from django.shortcuts import render
from .models import Equipo
from .forms import MemberForm

def list_equipo(request):
    
  all_equipo = Equipo.objects.all()
    
  context = {
    'equipo': all_equipo
  }
  
  return render(request, 'equipo/list_equipo.html', context)

def member_detail(request, id):
  member = Equipo.objects.get(id=id)
  context = {
    'member': member
  }
  return render(request, 'equipo/member_detail.html', context)

""" def create_member(request):
  if request.method == 'GET':      
    return render(request, 'equipo/create_member.html', context={})
  else:
    name = request.POST.get('name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    bio = request.POST.get('bio')
    position = request.POST.get('position')
    image = request.FILES.get('image')
    Equipo.objects.create(name = name, last_name = last_name, email = email, phone = phone, bio = bio, position = position, image = image)
    return render(request, 'equipo/create_member.html', context={}) """

def create_member(request):
  if request.method == 'GET':  
    form = MemberForm()    
    return render(request, 'equipo/create_member.html', context={'form': form})
  else:
    form = MemberForm(request.POST, request.FILES)
    if form.is_valid():
      data = form.cleaned_data
      Equipo.objects.create(name = data['name'], last_name = data['last_name'], email = data['email'], phone = data['phone'], bio = data['bio'], position = data['position'], image = data['image'])
      return render(request, 'equipo/create_member.html', context={})
    else:
      context = {
        'form': form,
        'message': form.errors
      }
      return render(request, 'equipo/create_member.html', context)


