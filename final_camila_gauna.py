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
    elif len(alumnosDesaprobados) != 0:
        print(f"Alumnos que desaprobaron: {alumnosDesaprobados}")

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
        print(
            f"{notasOrdenadas[0]['nombre']} es la única persona en el listado. Su promedio fue de: {notasOrdenadas[0]['promedio']}")
    else:
        print(
            f"La nota más alta la obtuvo {notasOrdenadas[-1]['nombre']} con promedio de: {notasOrdenadas[-1]['promedio']}")
        print(
            f"La nota más baja la obtuvo {notasOrdenadas[0]['nombre']} con promedio de: {notasOrdenadas[0]['promedio']}")

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
    elif len(encontrado) == 0:
        print("Su búsqueda no ha arrojado resultados.")


# Realizar una función que permita la carga de n alumnos. Por cada alumno se deberá preguntar el nombre completo
# y permitir el ingreso de 3 notas. Las notas deben estar comprendidas entre 0 y 10. Devolver el listado de alumnos.
def main():
    salir = "si"
    listado_alumnos = []
    while salir == "si":
        notas = []
        total = 0
        nombre = input("Ingrese el nombre completo del alumno: ")
        for i in range(3):
            nota = int(input("Nota: "))
            notas.append(nota)
            if (nota > 10):
                print("La nota debe estar comprendida entre 0 y 10. Por favor, vuelva a comenzar.")
                quit()
        for nota in notas:
            total += nota
        resultado = total / len(notas)
        promedio = round(resultado, 2)
        alumno = {'nombre': nombre, "notas": notas, "promedio": promedio}
        listado_alumnos.append(alumno)
        salir = input("Desea seguir cargando alumnos?: ")

    aprobador(listado_alumnos)
    promedioDelCurso(listado_alumnos)
    ordenadorDeNotas(listado_alumnos)
    busquedaDeAlumno = input("Ingrese el nombre del alumno que desea buscar: ")
    buscador(listado_alumnos, busquedaDeAlumno)

    return listado_alumnos


main()
