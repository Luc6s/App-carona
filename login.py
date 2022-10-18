

arq = open('registrado.txt', 'a')

print("Seja bem-vindo!")

def inicio():
    
    r = input("Deseja logar(1) ou se resgistrar(2) ou sair(3)?  ")
    
    if r == '1':       
        return acesso()
        
    elif r == '2':
        return registre()
    
    elif r == '3':       
        return 10
    
    elif r != '2' and r != '1':
        return inicio()

def acesso():
    
    print("Acesso: ")
    usuario = input('Digite o nome de usuário: ')
    usuario = usuario.strip()
    senha = input("Digite a senha: ")
    senha = senha.strip()
    
    if senha == "" or usuario == "":
        print("Inválido: Espaço em branco")
        return acesso()
    
    login = codigo(usuario) + "-" + codigo(senha)
    arq = open('registrado.txt') 
    registrados = arq.read()
    
    if login in registrados:
        print("Bem vindo")
        linha = abrir(login)
        dados = tradutor(linha)
        arq.close()
        return dados
            
    else:
        print("login inválido")
        return inicio()
        
def registre():
    
    usuario = input('Digite o nome de usuário: ')
    validar(usuario)
    senha = input("Digite a senha: ")
    if senha == "":
        print("Senha inválida: em branco. ")
        registre()
    email = input("Digite o email: ")
    validar(email)
    dre = input("Digite seu DRE: ")
    validar(dre)
    telefone = input("Digite seu telefone: ") 
    validar(telefone)
    diferente(usuario, senha, email, dre, telefone)
    if diferente == 1:
        return registre()
    login = ("\n" + codigo(usuario) + "-" + codigo(senha) + "-" + codigo(email) + "-" + codigo(dre) + "-" + codigo(telefone) + "-" + codigo("usuario") + "+")
    arq = open('registrado.txt', 'a')
    arq.write(login)
    arq.close()
    print("Cadastros feito com sucesso! ")
    return inicio()
    
def codigo(u):
    id = []  
    for letra in u:
        x = ord(letra) - 28
        id.append(str(x))
    
    id = "".join(id)
    return id

def diferente(a, b, c, d, e):
    if a == b or a == c or a == d or a == e or b == c or b == d or b == e or c == d or c == e or d == e:
        print("Um campo não pode ser igual aos demais. ")
        return 0
    else:
        return 1
        

def validar(e):
    e = e.strip()
    e = codigo(e)
    arq = open('registrado.txt') 
    registrados = arq.read()
    if e == "" or e in registrados:
        print("Inválido; em branco ou já existente.")
        arq.close()
        registre()
    else:
        return 0
    
def tradutor(codigo):
    y = 1
    palavra = ""
    x = 0
    letra = [] 
    tudo = []
    for a in codigo:
        if a == "+":
            break
        if a == "-" or a == codigo[-1]:
            tudo.append(palavra)
            palavra = ""
            y = 0
            x = 0
        if y > 0:    
            letra.append(a)
            x = x + 1
        if (x % 2) == 0 and x != 0:
            letra = int((''.join(letra))) + 28
            letra = chr(letra)
            palavra = palavra + letra
            letra = []
            x = 0
        y = 1

    return tudo

def abrir(t):
    with open("registrado.txt", 'r') as fp:
        lines = fp.readlines()
        for line in lines:
            if line.find(t) != -1:
                return line



arq.close()

    
