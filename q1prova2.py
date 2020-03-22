chapa=[]
codigo=[]
nome=[]
voto=[]
titulo=[]
def lin():
    print('-'*50)
while True:
    lin()
    print('     MENU:  ')
    lin()
    print('''
    [0]-Finalizar Programa
    [1]-Cadastrar Chapa
    [2]-Cadastrar Voto
    [3]-Exibir Apuração da Eleição
    [4]-Exibir Chapa Vencedora''')

    opc=int(input("Informe a opção desejada: "))
    if opc==0:
        break
    elif opc==1:
        chapa=(str(input("Informe o nome da Chapa: ")))
        if chapa in nome:
            print("Chapa ja cadastrada!")
        else:
            nome.append(chapa)
            voto.append(0)
        cod=(int(input("Informe o codigo: ")))
        if cod in codigo:
            print("Cod ja cadastrado!")
        else:
            codigo.append(cod)
        
    elif opc==2:
        titulo.append(int(input("Informe o titulo do aluno: ")))
        nomeA=str(input("Informe nome do Aluno: "))
        codA=int(input("Informe o cod da chapa escolhida: "))
        if codA in codigo:
            voto[codigo.index(codA)] += 1
            print("Voto registrado!")
        else:
            print("Voto Invalido! ")
            
    elif opc==3:
        lin()        
        print("Relatorio de Apuração dos votos")
        lin()
        print(f"Cod.        Nome da Chapa:       Votos:")
        for i in range(len(codigo)):
            print(f"{codigo[i]}              {nome[i]}              {voto[i]}")
    elif opc==4:
        a=0
        maior= max(voto)
        for i in range(len(voto)):
            if maior== voto[i]:
                a=a+1
                Mvoto = nome[i]
        if a==1:
            print(f"Chapa Vencedora foi: {Mvoto}")


        

