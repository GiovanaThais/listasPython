cad=[]
nome=['']
idd=[]
numMat=[]
numPar=[]
numImpar=[]
iddM=[]
iddN=[]
totmai=totmen=0
for i in range(0,3):
    nome=str(input("Nome: "))
    idd=int(input("Idade: "))
    numMat=int(input("Informe numero de matricula: "))
    cad.append(nome)
    cad.append(idd)
    cad.append(numMat)
    if idd >=20:
        iddM.append(nome)
        totmai+=1
    else:
        iddN.append(nome)
        totmen+=1
    if numMat%2==0:
        numPar.append(nome)
    else:
        numImpar.append(nome)
print(f"n de pessoas cadastraas:{len(nome)}") 
print(f"{iddM} é maior de idade ")
print(f'{iddN} é menor de idade')
print(f"total de maiores:{totmai} e de menores {totmen}")
print(f"candidatos com numero de matricula par: {numPar}")
print(f"candidatos com numero de matricula impar: {numImpar}")
   