# Definir una función que dado un listado de alumnos evalúe cuántos aprobaron y cuantos desaprobaron,
# teniendo en cuenta que se aprueba con 4. La nota será el promedio de las 3 notas para cada alumno.
def aprobador(listado):
    alumnosAprobados = []
    alumnosDesaprobados = []
    for alumno in listado:
        promedioAlumno = alumno["promedio"]
        if promedioAlumno >= 4:
            alumnosAprobados.append(alumno)
        else:
            alumnosDesaprobados.append(alumno)
    if len(alumnosAprobados) != 0:
        print(f"Alumnos que aprobaron: {alumnosAprobados}")
    elif len(alumnosAprobados) == 0:
        print("Ningún alumno aprobó.")
    if len(alumnosDesaprobados) != 0:
        print(f"Alumnos que desaprobaron: {alumnosDesaprobados}")
    elif len(alumnosDesaprobados) == 0:
        print("Ningún alumno desaprobó.")

# Informar el promedio de nota del curso total.
def promedioDelCurso(listado):
    total = 0
    for alumno in listado:
        total += alumno["promedio"]
    promedio = total / len(listado)
    resultado = round(promedio, 2)
    print(f"El promedio del curso fue de: {resultado}")

# Realizar una función que indique quien tuvo el promedio más alto y quien tuvo la nota promedio más baja.
def ordenadorDeNotas(listado):
    notasOrdenadas = sorted(listado, key=lambda x: x['promedio'])
    if len(notasOrdenadas) == 1:
        print(f"{notasOrdenadas[0]['nombre']} es la única persona en el listado. Su promedio fue de: {notasOrdenadas[0]['promedio']}")
    else:
        print(f"La nota más alta la obtuvo {notasOrdenadas[-1]['nombre']} con promedio de: {notasOrdenadas[-1]['promedio']}")
        print(f"La nota más baja la obtuvo {notasOrdenadas[0]['nombre']} con promedio de: {notasOrdenadas[0]['promedio']}")

# Realizar una función que permita buscar un alumno por nombre, siendo el nombre completo o parcial,
# y devuelva una lista con los n alumnos que concuerden con ese nombre junto con todos sus datos,
# incluido el promedio de sus notas.
def buscador(listado, busqueda):
    encontrado = []
    for alumno in listado:
        if busqueda in alumno["nombre"]:
            encontrado.append(alumno)
    if len(encontrado) != 0:
        print(f"Estos fueron los resultados de tu búsqueda: {encontrado}")
    else:
        print("Su búsqueda no ha arrojado resultados.")
    return "ok"

# Realizar una función que permita la carga de n alumnos. Por cada alumno se deberá preguntar el nombre completo
# y permitir el ingreso de 3 notas. Las notas deben estar comprendidas entre 0 y 10. Devolver el listado de alumnos.
def main():
    salir = "si"
    listado_alumnos = []
    bienvenida = input("""
                                       ***Bienvenido al programa de gestión de notas del colegio***
                        Por cada alumno se le requerirá que ingrese 3 notas que deberán estar comprendidas entre 0 y 10.
                                            PARA COMENZAR ESCRIBA "OK" y presione la tecla ENTER: """)
    if bienvenida != "ok":
        quit()
    if bienvenida == "ok":
        while salir == "si":
            notas = []
            total = 0
            nombre = input("Ingrese el nombre completo del alumno: ")
            for i in range(3):
                nota = int(input("Nota: "))
                while nota not in range(0,11):
                    print("La nota debe estar comprendida entre 0 y 10. Por favor, vuelva a ingresar la nota: ")
                    nota = int(input("Nota: "))
                    if nota in range(0,11):
                        break
                notas.append(nota)
            for nota in notas:
                total += nota
            resultado = total / len(notas)
            promedio = round(resultado, 2)
            alumno = {'nombre': nombre, "notas": notas, "promedio": promedio}
            listado_alumnos.append(alumno)
            salir = input("¿Desea seguir cargando alumnos? (Si/No): ")

        aprobador(listado_alumnos)
        promedioDelCurso(listado_alumnos)
        ordenadorDeNotas(listado_alumnos)
#lógica de ayuda para la función buscador(): 
#si en la búsqueda no se encuentran resultados se va a preguntar si desea seguir buscando
#si responde que "si" se vuelve a ejecutar la búsqueda
#si responde que "no" se finaliza el programa.
        busquedaDeAlumno = input("Ingrese el nombre del alumno que desea buscar: ")
        salida = "si"
        while (buscador(listado_alumnos, busquedaDeAlumno) == "ok" and salida == "si"):
            salida = input("¿Desea realizar una nueva búsqueda? (Si/No): ")
            if (salida == "si"):
                busquedaDeAlumno = input("Ingrese el nombre del alumno que desea buscar: ")
            elif (salida == "no"):
                print("Gracias por utilizar el sistema de gestión de notas.")
                quit()

    return listado_alumnos
main()