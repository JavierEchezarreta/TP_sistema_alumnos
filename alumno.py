from persona import Persona

class Alumno(Persona):
    def __init__(self):
        super().__init__()
        self.nombre_curso = ''
        
    def ingresar_alumno(self):
        self.agregar_persona()
        self.nombre_curso = input('Ingrese el curso al que desea anotar el alumno: ')
        while self.nombre_curso.isalpha() is False:
            self.nombre_curso = input('Nombre incorrecto, intente nuevamente ')