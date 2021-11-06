#!/usr/bin/env python
# coding: utf-8

from prettytable import PrettyTable

#Contadores de productos
countCamiseta = 10
countPantalon = 20
countZapatos = 32
countChaqueta = 6
countGorra = 40

lista = [
    #Nombre, Precio, ID, Caracteristicas, Cantidad
    ["Camiseta", 50000, 1, ("negra", "algodón"),countCamiseta],
    [ "Pantalón", 55000, 2, ("Azul", "Casual"), countPantalon], 
    ["Zapatos", 200000, 3, ("Azules", "deportivos"), countZapatos], 
    ["Chaqueta", 150000, 4, ("Roja", "Casual"),countChaqueta], 
    ["Gorra", 45000, 5, ("Negra", "Deportiva"),countGorra]
    ]

#Creación de un Switch Case que recibe de argumento ID y devuelve el producto
class Productos:
    def switch(self, ID):
        default =  "Producto no existe"
        return getattr(self, "p_" + str(ID), lambda: default)()
    
    def p_1(self):
        producto = "Camiseta"
        return(producto)
    def p_2(self):
        producto = "Pantalón"
        return producto
    def p_3(self):
        producto = "Zapatos"
        return(producto)
    def p_4(self):
        producto = "Chaqueta"
        return producto
    def p_5(self):
        producto = "Gorra"
        return producto
    

#Creando el almacén, ID = Producto
class SedeBogota:
    
    def __init__(self, ID): #ID = producto

        self.ID = Productos().switch(ID)  #SwitchCase
        #self.producto = Productos()
        #sedeBogota.p -= 1
        
    def seleccion(self):
        print("Ha seleccionado el producto", self.ID)
              
    def comprar(self):
        print(f"El producto {self.ID} ha sido adquirido")
        
    def cantidadProducto(self):
        global countCamiseta, countPantalon, countZapatos, countChaqueta, countGorra, lista
        
        if self.ID == "Camiseta":
            countCamiseta -= 1
            (lista[0])[4] = countCamiseta #El elemento de n4 del elemento n0 de la lista
            mostrarTabla()
            print(f"Ahora quedan {countCamiseta} {self.ID} disponibles")
        elif self.ID == "Pantalón":
            countPantalon -=1
            (lista[1])[4] = countPantalon
            mostrarTabla()
            print(f"Ahora quedan {countPantalon} {self.ID} disponibles")
        elif self.ID == "Zapatos":
            countZapatos -= 1
            (lista[2])[4] = countZapatos
            mostrarTabla()
            print(f"Ahora quedan {countZapatos} {self.ID} disponibles")
        elif self.ID == "Chaqueta":
            countChaqueta -=1
            (lista[3])[4] = countChaqueta
            mostrarTabla()
            print(f"Ahora quedan {countChaqueta} {self.ID} disponibles")
        else:
            countGorra -=1
            (lista[4])[4] = countGorra
            mostrarTabla()
            print(f"Ahora quedan {countGorra} {self.ID} disponibles")

##
def mostrarTabla():
    global lista

    t = PrettyTable(["Nombre", "Precio", "ID", "Caracteristicas", "Cantidad"]) #Se crean las cabeceras
    for elements in lista:
        t.add_row(elements) #se añaden las filas
    
    print(t)

print("Están disponibles los siguientes productos:")
mostrarTabla()

ID = int(input("\nInserte el ID del producto que quiere comprar: "))

#producto = Productos.switch(ID)

producto = SedeBogota(ID)
producto.seleccion()
producto.comprar()
producto.cantidadProducto()

#l = lista[0]
#print(l[4])