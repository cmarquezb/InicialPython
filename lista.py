lista = [1,30,2,3,7,5,23,16]
aux=0
# ordenamiento burbuja
print(lista)
for i in range(1,len(lista)):
    for j in range(0,len(lista)-i):
        if lista[j]>lista[j+1]:
            aux=lista[j]
            lista[j]=lista[j+1]
            lista[j+1]=aux
print(lista)

lista2 = [1,30,2,3,7,5,23,16]
# ordenamiento por seleccion

print(lista2)
for i in range(0,len(lista2)-1):
    aux=i
    for j in range(i+1,len(lista2)):
        if lista2[j]<lista2[aux]:
            aux=j
    aux2=lista2[i]
    lista2[i]=lista2[aux]
    lista2[aux]=aux2
print(lista2)

