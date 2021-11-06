from prettytable import PrettyTable

countCamiseta = 100
countJogger = 70
countChanclas = 400
countBuzo = 99
countMaleta = 200

lista = [
    #Nombre, Precio, ID, Caracteristicas, Cantidad
    ["Camiseta", 90000, 1, ("negra", "algodón"),countCamiseta],
    [ "Jogger", 100000, 2, ("Azul", "Casual"), countJogger], 
    ["Chanclas", 155000, 3, ("Azules", "deportivos"), countChanclas], 
    ["Buzo", 255500, 4, ("Roja", "Casual"),countBuzo], 
    ["Maleta", 85000, 5, ("Negra", "Deportiva"),countMaleta]
    ]

class Productos:
    def switch(self, ID):
        default =  "Producto no existe"
        return getattr(self, "p_" + str(ID), lambda: default)()
    
    def p_1(self):
        producto = "Camiseta"
        return(producto)
    def p_2(self):
        producto = "Jogger"
        return producto
    def p_3(self):
        producto = "Chanclas"
        return(producto)
    def p_4(self):
        producto = "Buzo"
        return producto
    def p_5(self):
        producto = "Maleta"
        return producto
    

class SedeMedellin:
    
    def __init__(self, ID): #ID = producto

        self.ID = Productos().switch(ID) #SwitchCase
        
    def seleccion(self):
        print("Ha seleccionado el producto", self.ID)
              
    def comprar(self):
        print(f"El producto {self.ID} ha sido adquirido")
        
    def cantidadProducto(self):
        global countCamiseta, countJogger, countChanclas, countBuzo, countMaleta, lista
        
        if self.ID == "Camiseta":
            countCamiseta -= 1
            (lista[0])[4] = countCamiseta
            mostrarTabla()
            print(f"Ahora quedan {countCamiseta} {self.ID} disponibles")
        elif self.ID == "Jogger":
            countJogger -=1
            (lista[1])[4] = countJogger
            mostrarTabla()
            print(f"Ahora quedan {countJogger} {self.ID} disponibles")
        elif self.ID == "Chanclas":
            countChanclas -= 1
            (lista[2])[4] = countChanclas
            mostrarTabla()
            print(f"Ahora quedan {countChanclas} {self.ID} disponibles")
        elif self.ID == "Buzo":
            countBuzo -=1
            (lista[3])[4] = countBuzo
            mostrarTabla()
            print(f"Ahora quedan {countBuzo} {self.ID} disponibles")
        else:
            countMaleta -=1
            (lista[4])[4] = countMaleta
            mostrarTabla()
            print(f"Ahora quedan {countMaleta} {self.ID} disponibles")

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

producto = SedeMedellin(ID)
producto.seleccion()
producto.comprar()
producto.cantidadProducto()