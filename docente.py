from persona import Persona

class Docente(Persona):
    def __init__(self):
        super().__init__()
        self.nombre_curso = ''
        self.horario = ''
        
        
    def ingresar_docente(self):
        self.agregar_persona()
        self.nombre_curso = input('Ingrese el curso del docente: ')
        while self.nombre_curso.isalpha() is False:
            self.nombre_curso = input('Nombre incorrecto, intente nuevamente ')
        self.horario = input('Ingrese el horario del curso: ')
        
        


