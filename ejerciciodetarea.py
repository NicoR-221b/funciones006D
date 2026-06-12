#Ejercicio 7
#Un restaurante necesita un sistema que calcule el monto de propina según el
#porcentaje seleccionado por el cliente (10%, 15% o 20%), y muestre el desglose:
#subtotal, propina y total a pagar.
#🎯 Objetivo Crear funciones para calcular y mostrar el desglose de una cuenta con propina,
#usando return para comunicar resultados entre funciones.
#💡 Concepto Comunicación entre funciones mediante return

#Funcionesssssss
def mostrar_encabezado():
    print ("||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||")
    print ("||     Sistema de registro     ||")
    print ("||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||")

def desglose(): 
    while True:
        try:
            sub = int(input("Ingrese el monto a pagar:  "))
            if sub <= 0:
                print ("Ingrese un valor válido (no puede ser 0 o negativo)")
                continue
            else: 
                break 
            
        except ValueError:
            input("Ingrese un monto válido")

    while True:
        try:
            propina = int(input("Seleccione cuanto porcentaje de propina desea agregar (10% / 15% / 20%): ")) 
            if propina != 10 and propina != 15 and propina != 20:
                print ("Descuento fuera de las opciones.")
                continue 
            if sub <= 0:
                print ("Ingrese un valor válido (no puede ser 0 o negativo)")
                continue
            else: 
                break 
            
        except ValueError:
            input("Ingrese un monto válido")

    porcentaje = sub*propina/100 
    total_pagar = sub + porcentaje

    datos_cuenta = {}
    datos_cuenta["Subtotal"] = sub
    datos_cuenta["Propina"] = porcentaje
    datos_cuenta["Total"] = total_pagar
    return datos_cuenta

def mostrar_ficha(datos_cuenta):
    print (f"SU SUBTOTAL ES DE: {datos_cuenta["Subtotal"]}")
    print (f"SU PROPINA SERÍA DE: {datos_cuenta["Propina"]}")
    print (f"SU TOTAL A PAGAR ES DE: {datos_cuenta["Total"]}")


#codigo principal

mostrar_encabezado()
datos = desglose()
mostrar_ficha (datos)

      





    


