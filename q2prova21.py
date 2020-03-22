nome=[]
tel=[]
agenda=[]
def lin():
    print('-'*50)
while True:
    nome.append(str(input("Informe o nome: ")))
    tel.append(int(input("Informe o numero do telefone: ")))
    agenda.append([nome,tel])
    resp=str(input("Deseja cadastrar mais pessoas?(S/N):")).upper()
    if resp=='N':
        break
lin()
while True:
    opc=str(input("Informe o nome da pessoa q deseja ver o numero (digite F para finalizar programa):"))
    if opc=='F':
        break
    if opc in nome:
        for i in range(len(nome)):
            if opc==nome[i]:
                print(f'Nome : {nome[i]}')
                print(f'tel: {tel[i]}')   
    else:
        print("Nome não cadastrado")