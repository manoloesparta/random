# -*- coding: utf-8 -*-
class Scout:
    def __init__(self, nombre, apellidos, nacimiento, cum, vigencia_registro, seccion=None):
        self.nombre = nombre
        self.apellidos = apellidos
        self.nacimiento = nacimiento
        self.cum = cum
        self.vigencia_registro = vigencia_registro
        self.seccion = seccion