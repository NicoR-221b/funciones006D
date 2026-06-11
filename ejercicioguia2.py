#Funciones
def convertir_calificacion(puntaje, puntaje_total):
    nota = ((puntaje * 6 / puntaje_total) + 1)
    return round(nota, 1)





#codigo principal

while True: 
    try: 
        p = float(input("Ingrese el puntaje del estudiante: "))
        if p < 0:
            print("Debe ser dato válido.!!")
        else:
            break
    except ValueError:
        print ("Ingrese un dato válido")
while True: 
    try:
        pt = float(input("Ingrese el puntaje total:  "))
        if pt < 0:
            print("Debe ser un numero positivo.!!")
        else:
            break
    except ValueError: 
        print ("ingrese un dato válido. ")


#llamar a la funcion
calif = convertir_calificacion(p, pt)
print (f"La calificacion en escala Chilena es: {calif}")





