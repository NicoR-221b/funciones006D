#funciionessss

def mostrar_encabezado():
    print ("||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||")
    print ("|| Sistema de registro escolar ||")
    print ("||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||")

def datos_estudiante():
    nombre = input("Ingrese su nombre: ")
    while True:
        try:
            semestre = int(input("Ingrese el semestre que está cursando: "))
            if semestre < 1 or semestre > 5:
                print("Debe de ingresar un semestre del 1 al 5")
            else:
                break
        except ValueError:
            print("Debe ingresar Números")

    carrera = input("Ingrese la carrera que está cursando:")
    rut = input("Ingrese el rut del estudiante: ")

    estudiante = {}
    estudiante["nombre"] = nombre
    estudiante["semestre"] = semestre
    estudiante["carrera"] = carrera 
    estudiante["Rut"] = rut 
    return estudiante 

def mostrar_ficha (estudiante):
    print (f"Nombre del estudiante: {estudiante["nombre"]}")
    print (f"RUT del estudiante: {estudiante["rut"]}")
    print (f"Carrera del estudiante: {estudiante["carrera"]}")
    print (f"Semestre del estudiante: {estudiante["semestre"]}")


#codigo principaallllllll

datos = datos_estudiante()
mostrar_encabezado()
mostrar_ficha(datos)