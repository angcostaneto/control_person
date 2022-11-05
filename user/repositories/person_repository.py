from http.client import BAD_REQUEST
from django.core.exceptions import ObjectDoesNotExist

from user.entities.person_entity import PersonEntity
from user.models import Person


class PersonRepository:

  def get_by_id(self, reference):
    try:
      return Person.objects.get(id=reference)

    except ObjectDoesNotExist:
      return None

  def create(self, first_name: str, last_name: str, rg: str, cpf: str):  
    try:
      return Person.objects.create(
        first_name = first_name,
        last_name = last_name,
        rg = rg,
        cpf = cpf
      )

    except BAD_REQUEST:
      return None