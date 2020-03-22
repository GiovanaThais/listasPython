labs=[]
comps=[]
labMax=[]
labMin=[]

qntSalas=int(input("Informe a quantidade de labs: "))
for i in range(qntSalas):
    nomLab=str(input("Informe a identificação do lab:"))
    qntComp=int(input("Informe a quantidade de computadores: "))
    comps.append(qntComp)
    labs.append(nomLab)
    if qntComp==max(comps):
        labMax.append(nomLab)
    if qntComp==min(comps):
        labMin.append(nomLab)
        
print("A media de computadores por sala: ",sum(comps)/(qntSalas))
print("Maior quantidade de computadores: ",max(comps))
print(f"Laboratorio com mais de {max(comps)} computadores: {labMax}")
print("Menor quantidade de computadores por sala: ",min(comps))
print(f"Laboratorios com {min(comps)} computadores: {labMin}")
