from user.repositories.person_repository import PersonRepository
from user.use_cases.get_person_case.get_person_case import GetPersonCase
from user.use_cases.use_case_factory import UseCaseFactory


class GetPersonCaseFactory(UseCaseFactory):
  def factory(self) -> GetPersonCase:
    person_repository = PersonRepository()
    return GetPersonCase(person_repository)

