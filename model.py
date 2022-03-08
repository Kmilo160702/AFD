from real import Real
from entero import Entero
from mail import Email
from id import Identificador


class Model:
    def __init__(self) -> None:
        pass

    def verifyEmail(self, value):
        return Email().automataEmail(value)

    def verifyEntero(self, value):
        return Entero().automataEntero(value)

    def verifyReal(self, value):
        return Real().automataReal(value)

    def verifyId(self, value):
        return Identificador().automataId(value)
