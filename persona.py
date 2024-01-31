import re

def validar_email(email):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(patron, email):
        return True
    else:
        return False
    
def validar_telefono(telefono):
    if len(telefono) == 10 and telefono.isnumeric():
            return True
    return False

class Persona:
    def __init__(self):
        self.nombre = ''
        self.apellido = ''
        self.direccion = ''
        self.email = ''
        self.telefono = ''

    def agregar_persona(self):
        self.nombre = input('Ingrese el nombre: ')
        while self.nombre.isalpha() is False:
            self.nombre = input('Nombre incorrecto, intente nuevamente ')
        self.apellido = input('Ingrese el apellido: ')
        while self.apellido.isalpha() is False:
            self.apellido = input('Apellido incorrecto, intente nuevamente: ')
        self.direccion = input('Ingrese la dirección: ')
        self.email = input('Ingrese el email (ej: cuenta@gmail.com): ')
        while validar_email(self.email) is False:
            self.email = input('Email incorrecto, intente nuevamente: ')
        self.telefono = input("Ingrese su número de teléfono (ej: 3412785322): ")  
        while validar_telefono(self.telefono) is False:
            self.telefono = input("Número incorrrecto, intente nuevamente: ")   

