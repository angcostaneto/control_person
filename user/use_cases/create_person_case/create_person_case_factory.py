from user.infra.repositories.person_repository import PersonRepository
from user.use_cases.create_person_case.create_person_case import CreatePersonCase
from user.use_cases.use_case_factory import UseCaseFactory


class CreatePersonCaseFactory(UseCaseFactory):
  def factory(self) -> CreatePersonCase:
    person_repository = PersonRepository()
    return CreatePersonCase(person_repository)