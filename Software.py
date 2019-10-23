import os
os.system("cls")

# Definir productos y precios

productos = ["arrozcosteño", "cocacolapersonal", "inkakolapersonal", "chocolatesorrento", "snickers", "papaslays", "pringles", 
"detergenteariel", "galletascasino", "galletaschaplin", "chocolatevicio", "ajinosillao", "ketchupalacena", 
"cubosmaggie", "ajinomen"]
precios = [2.50,2.00,1.50,2.50,3.50,1.50,5.00,3.50,1.20,1.00,2.00,7.00,4.00,3.50,2.50]
stock = [20,15,15,16,12,25,25,10,14,5,10,15,10,20,50]


# Cuando el cajero digita los productos:

i = 0
while True:
    i+=1
    entrada=input("Ingrese el producto " + str(i) + " : ")
    entrada = entrada.lower()
    for p in productos:
        if (entrada == ""):
            print("Ingrese un producto ")
            break
        elif entrada != :
            print("El producto ha sido introducido erroneamente")
            break
    break

print(entrada)