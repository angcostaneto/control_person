from django.http import JsonResponse

from user.infra.repositories.person_repository import PersonRepository
from user.use_cases.base_use_case import BaseUseCase
from user.infra.dto.person_dto import PersonDto


class CreatePersonCase(BaseUseCase):
  def __init__(self, person_repository: PersonRepository) -> None:
    self._repository = person_repository

  def execute(self, first_name: str, last_name: str, rg: str, cpf: str):
    person = self._repository.create(first_name, last_name, rg, cpf)
    personDto = PersonDto(
      id=person.id,
      first_name= person.first_name,
      last_name= person.last_name,
      rg= person.rg,
      cpf= person.cpf
    )

    return JsonResponse(personDto.__dict__)
