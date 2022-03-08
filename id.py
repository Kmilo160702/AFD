from identificar import Identificar_codigo_ascii as k


class Identificador:

    def __init__(self):
        self.estado = 0

    def automataId(self, texto):
        cadenaRechazada = False
        pos = 0
        while (not cadenaRechazada and pos < len(texto)):
            letra = ord(texto[pos])

            # inicio
            if(self.estado == 0):
                if(k.es_letra(letra)):
                    self.estado = 1
                else:
                    cadenaRechazada = True
                if(self.estado == 1):
                    if(k.es_letra(letra)):
                        self.estado = 2
                    if(k.es_digito(letra)):
                        self.estado = 2

            pos = pos + 1

        if(cadenaRechazada):
            return 'Id Invalido'
        if(self.estado == 2):
            return 'Id Valido'
