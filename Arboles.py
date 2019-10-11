#Arboles Binarios
class Nodo:
    def __init__(self, listacampos = None, derecha = None, izquierda = None):
        self.listacampos = listacampos #todos los cmpos que quisieramos DNI, Nombre, Apellido
        self.derecha = derecha
        self.izquierda = izquierda
        
    def __str__(self):
        return "%s" %(self.listacampos)
        #cadena de string %s
        #Si coloco mas de % separados por espacios referencio a varios campos y debo llamarlos en los parentesis
        #Ejemplo Return "%s %s %s" %(self.DNI, self.Nombre, Self.Apellido) 
class Arbolito:
    def __init__(self):
        self.nodo_raiz = None   
        #self.derecha = None
        #self.izquierda = None

    def agregar(self,elemento_arbol):
        if self.nodo_raiz == None:
            self.nodo_raiz = elemento_arbol
        else:   
            aux = self.nodo_raiz
            padre = None
            while aux != None:
                padre = aux
                if self.nodo_raiz != None:
                    if elemento_arbol.listacampos < aux.listacampos:
                        aux = aux.izquierda         
                    else:
                        aux = aux.derecha
            if elemento_arbol.listacampos < padre.listacampos:
                padre.izquierda = elemento_arbol
            else:
                padre.derecha = elemento_arbol     

    # Preorden ingreso            
    def preorden(self,elemento_arbol):       
        if elemento_arbol != None:
            print(elemento_arbol)
            self.preorden(elemento_arbol.izquierda)
            self.preorden(elemento_arbol.derecha)
            
  # Inorden ingreso            
    def inorden(self,elemento_arbol):       
        if elemento_arbol != None:            
            self.inorden(elemento_arbol.izquierda)
            print(elemento_arbol)
            self.inorden(elemento_arbol.derecha)

  # Post orden ingreso            
    def postorden(self,elemento_arbol):       
        if elemento_arbol != None:            
            self.postorden(elemento_arbol.izquierda)           
            self.postorden(elemento_arbol.derecha)
            print(elemento_arbol)
    def GetRaiz(self):
        return self.nodo_raiz         
                
# menu inicial
if __name__ == "__main__":
    lista = Arbolito()
    while(True):
        print("**********MENÚ*********\n"+
            "1.- Agregar\n"+
            "2.- Pre Orden\n"+
            "3.- In Orden\n"+    
            "4.- Post Orden \n"+
            "5.- Salir")
        num = input("ingrese la option: ")
        if (num == "1"):
            Elcampo = input("ingrese el Nombre: ")
            nod=Nodo(Elcampo)
            lista.agregar(nod)
        elif(num == "2"):
            lista.preorden(lista.GetRaiz())
        elif(num == "3"):
            lista.inorden(lista.GetRaiz())    
        elif(num == "4"):
            lista.postorden(lista.GetRaiz())
        elif(num == "5"):
            exit()