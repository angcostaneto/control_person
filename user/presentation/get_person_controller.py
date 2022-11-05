from user.use_cases.get_person_case.get_person_case_factory import GetPersonCaseFactory
from django.http import request


def get_person(http_request: request, user_id):
  factory = GetPersonCaseFactory()
  return factory.execute(user_id)
