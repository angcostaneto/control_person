from django.urls import path
from user.presentation.get_person_controller import get_person
from user.presentation.create_person_controller import create_person

urlpatterns = [
  path('person/<uuid:user_id>', get_person, name='person'),
  path('create_person', create_person, name='create_person'),
]