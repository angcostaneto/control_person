class PersonEntity(object):
  def __init__(
    self,
    first_name,
    last_name,
    rg,
    cpf
  ):
    self._first_name = first_name
    self._last_name = last_name
    self._rg = rg
    self._cpf = cpf

  @property
  def first_name(self):
    return self._first_name

  @property
  def last_name(self):
    return self._last_name

  @property
  def rg(self):
    return self._rg

  @property
  def cpf(self):
    return self._cpf
