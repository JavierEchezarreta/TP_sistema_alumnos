from alumno import Alumno
from docente import Docente
from curso import Curso

cursos = []

def menu():
    print("\n--- MENÚ ---")
    print("1. Agregar curso")
    print("2. Ingresar docente")
    print("3. Inscribir alumno")
    print("4. Mostrar alumnos por curso")
    print("5. Buscar docente por curso")
    print("6. Asignar docente por curso")
    print("0. Salir")
   
lista_cursos = []
lista_docentes = []
     
while True:
    menu()
    opcion = input("Ingrese una opción: ")


    if opcion == "1":
        curso = Curso()
        curso.ingresar_curso()
        lista_cursos.append(curso)
        print("Curso agregado exitosamente.")

    elif opcion == "2":
        docente = Docente()
        docente.ingresar_docente()
        lista_docentes.append(docente)
        print("Docente agregado exitosamente.")
    
    elif opcion == "3":
        alumno = Alumno()
        alumno.ingresar_alumno()
        nombre_curso = alumno.nombre_curso
        for x in lista_cursos:
            if x.nombre == nombre_curso:
                x.anotar_alumno(alumno)    
        print('Alumno inscripto exitosamente.')
        
    elif opcion == '4':
        nombre_curso = input('Ingrese el nombre del curso: ').capitalize()
        for x in lista_cursos:
            if x.nombre == nombre_curso:
                x.mostrar_alumnos()
        
    elif opcion == '5':
        nombre_curso= input('Ingrese el nombre del curso: ').capitalize()
        for x in lista_cursos:
            if x.nombre == nombre_curso:
                x.buscar_docente()
        
    elif opcion == '6':
        nombre_curso = input('Ingrese el nombre del curso al que desea asignar un docente: ').capitalize()
        for x in lista_cursos:
            if x.nombre == nombre_curso:
                x.asignar_docente()
    
    elif opcion == '0':
        print('Gracias por usar el programa.')
        break
        
    else:
        print('Opcion inválida, intenten nuevamente.')
        
