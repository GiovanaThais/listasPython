import os.path

def cad():
    erros = 0
    print("-"*40)

    mat = input('Matrícula: ')
    nome = str(input("Nome: "))
    email = input('Email: ')
    tel = input("Telefone: ")
    cel = input('Celular: ')
    endereco = input("Endereço: ")
    num = input('Número: ')
    bairro = input('Bairro: ')
    city = input("Cidade: ")
    uf = input('UF: ')
    comp = input("Complemento: ")
    cargo = input('Cargo: ')
    salario = float(input('Salário: '))
    setor = input('Setor: ')
    sal_L = float(input("Salário líquido: "))
    inss = input("INSS: ")
    irrf = input(('IRRF: '))
    
    print("-"*40)

    if '@' not in email:
        print("Email inválido!")
        erros += 1
        
    
    if len(cel) < 8 : 
        print("Número de celular invalido!")
        erros+=1

    if len(tel) < 8 :
        print("Número de telefone invalido!")
        erros+=1 


    if erros == 0:
        setor_in = False
        arq_cad = open('listaCadastrados.txt', 'a')
        arq_cad.write(f"Numero de matricula:{mat}")
        arq_cad.write(f'\n Nome:  {nome}')
        arq_cad.write(f"\n Email: {email}")
        arq_cad.write(f'\n telefone: {tel}')
        arq_cad.write(f'\n celular: {cel}')
        arq_cad.write(f"\n Endereço: {endereco}")
        arq_cad.write(f'\n Numero: {num}')
        arq_cad.write(f'\n bairro: {bairro}')
        arq_cad.write(f'\n cidade: {city}')
        arq_cad.write(f'\n UF: {uf}')
        arq_cad.write(f'\n complemento: {comp}')
        arq_cad.write(f'\n cargo: {cargo}')
        arq_cad.write(f'\n setor: {setor}')
        arq_cad.write(f'\n salario: {salario}')
        arq_cad.write(f'\n salario liquido: {sal_L}')
        arq_cad.write(f'\n INSS: {inss}')
        arq_cad.write(f'\n IRRF: {irrf}\n\n')
        arq_cad.close()
        if os.path.exists('custoPorSetor.txt') == True:
            arq_custos = open('custoPorSetor.txt', 'r')
            texto = arq_custos.read()
            if f'Setor {setor}: R$' in texto:
                setor_in = True
                arq_custos = open('custoPorSetor.txt', 'r')
                for linha in  arq_custos:
                    if f'Setor {setor}: R$' in linha:
                        a = linha.replace(f'Setor {setor}: R$',"")
                        salarioA = float(a.rstrip())
                        valor = salario + float(salarioA)
                        texto = texto.replace(f'Setor {setor}: R${salarioA}', f'Setor {setor}: R${str(valor)}')
            arq_custos = open('custoPorSetor.txt', 'w')
            arq_custos.write(texto)
            arq_custos.close()
            if setor_in == False:
                arq_custos = open('custoPorSetor.txt', 'a')
                arq_custos.write(f'{setor}: R${salario}\n')
                arq_custos.close()
        else:
            arq_custos = open('custoPorSetor.txt', 'w')
            arq_custos.write(f'{setor}: R${salario}\n')
            arq_custos.close()
        
    return erros

def listar():
    if os.path.exists('listaCadastrados.txt') == True:
        arq_cad = open('listaCadastrados.txt', 'r')
        texto = arq_cad.read()
        print(texto)
        return texto
        arq_cad.close()


def custos():
    if os.path.exists('custoPorSetor.txt') == True:
        arq_custos = open('custoPorSetor.txt', 'r')
        texto = arq_custos.read()
        print(texto)
        return texto
        arq_custos.close()

while True :
    print('-'*40)
    print('''Menu :
    [1]-Cadastrar Funcionário
    [2]-Listar Funcionários
    [3]-Custos por setor
    [4]-Sair''')
    opc=(int(input('opção desejada: ')))
    if opc==4:
        break
    elif opc==1:
        cad()
        os.system('cls' if os.name == 'nt' else 'clear')
    elif opc==2:
        listar()
        print('Pressione enter para voltar')
        input()
        os.system('cls' if os.name == 'nt' else 'clear')
    elif opc==3:
        custos()
        print('Pressione enter para voltar')
        input()
        os.system('cls' if os.name == 'nt' else 'clear')
    print('-'*40)