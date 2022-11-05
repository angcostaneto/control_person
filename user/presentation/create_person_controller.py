import json
from django.http import request

from user.use_cases.create_person_case.create_person_case_factory import CreatePersonCaseFactory


def create_person(http_request: request):
  if http_request.method == "POST":
    factory = CreatePersonCaseFactory()
    params = json.loads(http_request.body)
    return factory.execute(
      params['first_name'],
      params['last_name'],
      params['rg'],
      params['cpf']
    )
