from abc import ABC, abstractmethod


class UseCaseFactory(ABC):
  @abstractmethod
  def factory(self):
    pass

  def execute(self, *args):
    case = self.factory()
    return case.execute(*args)
