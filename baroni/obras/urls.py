from django.urls import path
from .views import list_obras, obra_detail, create_obra 

urlpatterns = [
  path('list-obras/', list_obras),
  path('obra-detail/<int:id>', obra_detail),
  path('create-obra/', create_obra), 
  #path('edit-alquiler/<int:id>', update_obra),
  #path('delete-obra/<int:id>', delete_obra),
]