#Funciones
def datos_producto(name, stock, price):
    print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")
    print("                                    ")
    print(f"** Nombre del producto: {name} **")
    print(f"** Precio del producto: {price} **")
    print(f"** Stock del producto: {stock} **")
    print("                                    ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")




#Codigo Principal

nombre = input("Ingrese el nombre del producto: ")

while True: 
    try: 
        precio = int(input("Ingrese el precio del producto: "))
        if precio <= 0:
            print("Debe ser un numero positivo.!!")
        else:
            break
    except ValueError:
        print ("Ingrese un dato válido")
while True: 
    try:
        stock = int(input("Ingrese el stock del producto: "))
        if stock < 0:
            print("Debe ser un numero positivo.!!")
        else:
            break
    except ValueError: 
        print ("ingrese un dato válido. ")


#llamar a la funcion
#se deben enviar los parametros en el orden exacto que los declaré al crear la función
datos_producto(nombre,stock,precio)

