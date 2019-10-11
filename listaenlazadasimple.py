#lista enlazada simple
class Nodo:
    def __init__(self, listacampos = None, siguiente = None):
        self.listacampos = listacampos #todos los cmpos que quisieramos DNI, Nombre, Apellido
        self.siguiente = siguiente
    def __str__(self):
        return "%s" %(self.listacampos)
        #cadena de string %s
        #Si coloco mas de % separados por espacios referencio a varios campos y debo llamarlos en los parentesis
        #Ejemplo Return "%s %s %s" %(self.DNI, self.Nombre, Self.Apellido) 
class Lsimplex:
    def __init__(self):
        self.nodo_cabecera = None
        self.nodo_final = None

    def agregar(self,elemento):
        if self.nodo_cabecera == None:
            self.nodo_cabecera = elemento
        if self.nodo_final != None:
            self.nodo_final.siguiente = elemento
        self.nodo_final = elemento

    def mostrar(self):
        aux = self.nodo_cabecera
        while aux != None:
            print(aux)
            aux = aux.siguiente

    def buscar(self, item):
        paso=item.listacampos
        actual = self.nodo_cabecera
        encontrado = False
        Posicion = 0
        while actual != None and not encontrado:            
            Posicion = Posicion + 1
            if (actual.listacampos == paso):
                encontrado = True
                print("El valor fue encontrado00000000")
            else:
                actual = actual.siguiente                
        if encontrado:
            print("El nodo fue encontrado: " + str(Posicion))  
        else:
            print("El nodo no pertenece a esta lista")  
        return encontrado

    def eliminar(self,item):
        paso=item.listacampos
        previo = None
        actual = self.nodo_cabecera
        encontrado = False
        Posicion = 0
        while actual != None and not encontrado:  
            Posicion = Posicion + 1
            if (actual.listacampos == paso):
                encontrado = True                
                previo.siguiente = actual.siguiente                
            else:
                previo = actual
                actual = actual.siguiente        
        return encontrado    
        
    def ordenar(self):
        actual = self.nodo_cabecera
        Posicion = 0
        # metodo burbuja
        while actual != None:
            Posicion = Posicion + 1
            adelante = actual.siguiente
            while adelante != None:
                if actual.listacampos > adelante.listacampos: 
                    aux = actual.listacampos 
                    actual.listacampos = adelante.listacampos      
                    adelante.listacampos = aux
                else: 
                    adelante = adelante.siguiente
            actual = actual.siguiente        
                          
        
# menu inicial
if __name__ == "__main__":
    lista = Lsimplex()
    while(True):
        print("**********MENÚ*********\n"+
            "1.- Agregar\n"+
            "2.- Listar\n"+
            "3.- Ordenar Burbuja\n"+
            "4.- Eliminar\n"+
            "5.- Buscar\n"+
            "6.- Salir")
        num = input("ingrese la option: ")
        if (num == "1"):
            Elcampo = input("ingrese el Nombre: ")
            nod=Nodo(Elcampo)
            lista.agregar(nod)
        elif(num == "2"):
            lista.mostrar()
        elif(num == "3"):
            lista.ordenar()
            lista.mostrar()
        elif(num == "4"):
            Elcampo = input("ingrese el Nombre a Eliminar: ")
            nod=Nodo(Elcampo)
            lista.eliminar(nod)
            lista.mostrar()            
        elif(num =="5"):
            Elcampo = input("ingrese el Nombre a busar: ")
            nod=Nodo(Elcampo)
            lista.buscar(nod)
        elif(num == "6"):
            exit()