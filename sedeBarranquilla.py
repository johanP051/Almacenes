from prettytable import PrettyTable

countBlazer = 20
countCorbata = 354
countZapatos = 444
countSombrero = 303
countGafas = 299

lista = [
    #Nombre, Precio, ID, Caracteristicas, Cantidad
    ["Blazer", 130000, 1, ("negra", "algodón"),countBlazer],
    [ "Corbata", 25000, 2, ("Azul", "Casual"), countCorbata], 
    ["Zapatos", 230000, 3, ("Azules", "deportivos"), countZapatos], 
    ["Sombrero", 99000, 4, ("Roja", "Casual"),countSombrero], 
    ["Gafas", 50000, 5, ("Negra", "Deportiva"),countGafas]
    ]

class Productos:
    def switch(self, ID):
        default =  "Producto no existe"
        return getattr(self, "p_" + str(ID), lambda: default)()
    
    def p_1(self):
        producto = "Blazer"
        return(producto)
    def p_2(self):
        producto = "Corbata"
        return producto
    def p_3(self):
        producto = "Zapatos"
        return(producto)
    def p_4(self):
        producto = "Sombrero"
        return producto
    def p_5(self):
        producto = "Gafas"
        return producto
    

class SedeBarranquilla:
    
    def __init__(self, ID): #ID = producto

        self.ID = Productos().switch(ID) #SwitchCase
        
    def seleccion(self):
        print("Ha seleccionado el producto", self.ID)
              
    def comprar(self):
        print(f"El producto {self.ID} ha sido adquirido")
        
    def cantidadProducto(self):
        global countBlazer, countCorbata, countZapatos, countSombrero, countGafas, lista
        
        if self.ID == "Blazer":
            countBlazer -= 1
            (lista[0])[4] = countBlazer
            mostrarTabla()
            print(f"Ahora quedan {countBlazer} {self.ID} disponibles")
        elif self.ID == "Corbata":
            countCorbata -=1
            (lista[1])[4] = countCorbata
            mostrarTabla()
            print(f"Ahora quedan {countCorbata} {self.ID} disponibles")
        elif self.ID == "Zapatos":
            countZapatos -= 1
            (lista[2])[4] = countZapatos
            mostrarTabla()
            print(f"Ahora quedan {countZapatos} {self.ID} disponibles")
        elif self.ID == "Sombrero":
            countSombrero -=1
            (lista[3])[4] = countSombrero
            mostrarTabla()
            print(f"Ahora quedan {countSombrero} {self.ID} disponibles")
        else:
            countGafas -=1
            (lista[4])[4] = countGafas
            mostrarTabla()
            print(f"Ahora quedan {countGafas} {self.ID} disponibles")

##
def mostrarTabla():
    global lista

    t = PrettyTable(["Nombre", "Precio", "ID", "Caracteristicas", "Cantidad"])
    for elements in lista:
        t.add_row(elements)
  
    print(t)

print("Están disponibles los siguientes productos:")
mostrarTabla()

ID = int(input("\nInserte el ID del producto que quiere comprar: "))

#producto = Productos.switch(ID)

producto = SedeBarranquilla(ID)
producto.seleccion()
producto.comprar()
producto.cantidadProducto()