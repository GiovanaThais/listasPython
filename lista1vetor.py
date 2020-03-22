#gerar numeros alearios 
from random import:
lista1=[]
lista2=[]
lista3=[]
for i in range(10):
    lista1.append(randint(1,20))
    lista2.append(randint(1,20))
lista3=lista1+lista2
print(''Menu: 
(1) Inserir um numero aleatorio na lista3
(2) Remover o ultimo numero da lista3
(3) Imprimir a soma dos numeros da lista3
(4) Imprimir a quantidade de numeros da lista3
(5) Imprimir lista1,lista2 e lista3
(0) Finalizzar o programa '')
opc=int(input("Digite a opção desejada: "))
while opc!=0:
    if opc==1:
        for j in range(1):
            lista3.append((randint(1,100))
            print(lista3)
    elif opc==2:
        del lista3[-1]
        print(lista3)
    elif opc==3:
        print(sum(lista3))
    elif opc==4:
        print(len(lista3))
    elif opc==5:
        print(sorted(lista1))
        print(sorted(lista2))
        print(sorted(lista3))

opc=int(input("Digite a opção desejada: "))