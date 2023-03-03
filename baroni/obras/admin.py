from django.contrib import admin
from .models import Obra
from equipo.models import Equipo
from clientes.models import Cliente

admin.site.register(Obra)
admin.site.register(Equipo)
admin.site.register(Cliente)
