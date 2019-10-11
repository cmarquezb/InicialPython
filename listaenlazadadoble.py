#lista enlazada simple
class Nodo:
    def __init__(self, listacampos = None, siguiente = None, anterior = None):
        self.listacampos = listacampos #todos los cmpos que quisieramos DNI, Nombre, Apellido
        self.siguiente = siguiente
        self.anterior = anterior
    def __str__(self):
        return "%s" %(self.listacampos)
        #cadena de string %s
        #Si coloco mas de % separados por espacios referencio a varios campos y debo llamarlos en los parentesis
        #Ejemplo Return "%s %s %s" %(self.DNI, self.Nombre, Self.Apellido) 
class Doblex:
    def __init__(self):
        self.nodo_cabecera = None
        self.nodo_final = None        

    def agregar(self,elemento):
        if self.nodo_cabecera == None:
            self.nodo_cabecera = self.nodo_final = elemento
            self.nodo_cabecera.siguiente = self.nodo_cabecera.anterior = None
            self.nodo_final.siguiente = self.nodo_final.anterior = None

        if self.nodo_final != None:
            if self.nodo_cabecera == self.nodo_final:
                self.nodo_cabecera.anterior = None
            aux = self.nodo_final          
            self.nodo_final = aux.siguiente = elemento
            self.nodo_final.anterior = aux
           
        #self.nodo_final = elemento

    def mostrarup(self):
        aux = self.nodo_cabecera
        while aux != None:
            print(aux)
            aux = aux.siguiente

    def mostrardonw(self):
        aux = self.nodo_final
        while aux != None and self.nodo_cabecera != None :
            print(aux)
            aux = aux.anterior
            
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
        actual = self.nodo_cabecera
        encontrado = False
        Posicion = 0
        while actual != None and not encontrado:  
            Posicion = Posicion + 1
            if (actual.listacampos == paso):
                encontrado = True 
                # tres casos inicio final e intermedio
                aux1 = actual.siguiente 
                aux2 = actual.anterior
                if actual == self.nodo_cabecera:                    
                    self.nodo_cabecera = aux1
                    #self.nodo_cabecera.anterior = None
                    break
                elif aux1 == None:
                    self.nodo_final = aux2
                    self.nodo_final.siguiente = None                    
                    break
                elif aux2 != None and aux1 != None:                    
                    actual = aux1
                    actual.anterior = aux2
                    aux2.siguiente = actual                                      
                    break                                  
            else:                
                actual = actual.siguiente                      
        return encontrado    
        
    def ordenar(self):
        # metodo burbuja enlace hacia atras
        actual = self.nodo_final
        while actual != None:            
            atras = actual.anterior
            while atras != None:
                if actual.listacampos > atras.listacampos: 
                    aux = actual.listacampos 
                    actual.listacampos = atras.listacampos      
                    atras.listacampos = aux
                else: 
                    atras = atras.anterior
            actual = actual.anterior  
        # metodo burbuja enlace hacia adelante
        actual = self.nodo_cabecera
        while actual != None:            
            adelante = actual.siguiente
            while adelante != None:
                if actual.listacampos > adelante.listacampos: 
                    aux = actual.listacampos 
                    actual.listacampos = adelante.listacampos      
                    adelante.listacampos = aux
                else: 
                    adelante = adelante.siguiente
            actual = actual.siguiente        
        actual = self.nodo_final
       

        
# menu inicial
if __name__ == "__main__":
    lista = Doblex()
    while(True):
        print("**********MENÚ*********\n"+
            "1.- Agregar\n"+
            "2.- Listar UP\n"+
            "3.- Listar Down\n"+    
            "4.- Ordenar Burbuja\n"+
            "5.- Eliminar\n"+
            "6.- Buscar\n"+
            "7.- Salir")
        num = input("ingrese la option: ")
        if (num == "1"):
            Elcampo = input("ingrese el Nombre: ")
            nod=Nodo(Elcampo)
            lista.agregar(nod)
        elif(num == "2"):
            lista.mostrarup()
        elif(num == "3"):
            lista.mostrardonw()    
        elif(num == "4"):
            lista.ordenar()
            lista.mostrarup()
        elif(num == "5"):
            Elcampo = input("ingrese el Nombre a Eliminar: ")
            nod=Nodo(Elcampo)
            lista.eliminar(nod)
            lista.mostrarup()            
        elif(num =="6"):
            Elcampo = input("ingrese el Nombre a busar: ")
            nod=Nodo(Elcampo)
            lista.buscar(nod)
        elif(num == "7"):
            exit()