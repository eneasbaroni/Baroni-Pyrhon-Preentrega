from django.urls import path
from .views import list_equipo, member_detail, create_member

urlpatterns = [
  path('list-equipo/', list_equipo),
  path('member-detail/<int:id>', member_detail),
  path('create-member/', create_member),
  #path('edit-member/<int:id>', update_member),
  #path('delete-member/<int:id>', delete_member),
]