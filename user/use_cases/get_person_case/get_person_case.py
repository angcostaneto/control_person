from user.dto.person_dto import PersonDto
from user.repositories.person_repository import PersonRepository
from django.http import JsonResponse, HttpResponse

from user.use_cases.base_use_case import BaseUseCase


class GetPersonCase(BaseUseCase):
  def __init__(self, person_repository: PersonRepository) -> None:
    self._repository = person_repository

  def execute(self, user_id):
    person = self._repository.get_by_id(user_id)
    personDto = PersonDto(
      id=person.id,
      first_name= person.first_name,
      last_name= person.last_name,
      rg= person.rg,
      cpf= person.cpf
    )

    return JsonResponse(personDto.__dict__)
