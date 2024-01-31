class Curso:
    def __init__(self):
        self.nombre = ''
        self.horario = ''
        self.lista_alumnos = []
        self.docente = ''
    
    def ingresar_curso(self):
        self.nombre = input('Ingrese el nombre del curso: ')
        while self.nombre.isalpha() is False:
            self.nombre = input('Nombre incorrecto, intente nuevamente: ')
        self.horario = input('Ingrese el horario del curso: ')
        
        
    def anotar_alumno(self, alumno):
        self.lista_alumnos.append(alumno)
    
    def asignar_docente(self):
        self.docente = input('Ingrese el nombre del docente: ')
        print('Docente asignado exitosamente')
        
    def mostrar_alumnos(self):
        print(f"Alumnos inscritos en el curso de {self.nombre}: ")
        for alumno in self.lista_alumnos:
            print(alumno.nombre, alumno.apellido)
            
    def buscar_docente(self):
        if self.docente != '':
            print(f'El docente del curso de {self.nombre} es: {self.docente}')
        else:
            print("No se ha asignado un docente para este curso.")