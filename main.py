from carona import *
from login import *
from datetime import date, datetime

def addc(m, t):
    
    m = str(m[0])
    m = m.strip()
    k = pesquisa(codigo(t), 0)
    j = pesquisa(codigo("usuario"), 0)
    z = set(k) & set(j)
    z = list(z)
    z = int(z[0])
    p = desejadas(t)
    
    if m not in p:
        
        with open("registrado.txt") as f:
            texto = f.readlines()[z]
            
        nova = texto.strip() + m + "+"
        arq2 = open('registrado.txt', 'r')
        
        arq2.close()
        alterar_linha(z, nova)
        print("Adicionada com sucesso! ")
        
    else:
        print("Essa carona já foi adicionada!   ")
        
    perfil(1)
    
           
def alterar_linha(index_linha,nova_linha):
    
    with open('registrado.txt','r') as f:
        texto = f.readlines()
    with open('registrado.txt','w') as f:
        for i in texto:
            if texto.index(i)==index_linha:
                f.write(nova_linha + '\n')
            else:
                f.write(i)

def desejadas(usuario):
    
    k = pesquisa(codigo(usuario), 0)
    j = pesquisa(codigo("usuario"), 0)
    z = set(k) & set(j)
    z = list(z)
    z = int(z[0])
    with open("registrado.txt") as f:
        texto = f.readlines()[z]
    h = show2(texto)    

    return h

def linhabranca():
    
    with open("registrado.txt", 'r') as fr:
        lines = fr.readlines()
  
        with open("registrado.txt", 'w') as fw:
            for line in lines:

                if line.strip('\n') != "":
                    fw.write(line)
            

def perfil(x):   
    
    atual()
    linhabranca()
    
    global dade
    if x == 0:
        dade = inicio()
        if dade == 10:
            print("Saindo!  ")
            exit()
             
    usuario = str(dade[0])
    s = inicio2(usuario)
    
    if s == 10:
        perfil(0)
    
    if s == "3":
        r = 0
        r = input("Deseja ver as caronas oferecidas(1), ver as caronas desejadas(2) ou voltar(3)?   ")
           
        if r == "1":
                
            menu(usuario)
            print("")
            
        elif r == "3":
            perfil(1)
            
        elif r == "2":
            
            menu2(usuario) 
    
        else:
            print("Resposta inválida")
            perfil(1)
            
    elif s == "2":
        
        p = input("Alguma preferência de ida ou volta? (s) ou (n)  ")
        p = p.strip()

        if p == "s":
            g = input("ida ou volta?    ")
            g = g.strip()
            
            
            if g == "ida":
                b, j = receber(g, usuario)
                print("")
                abrirl(b)
                print("")
                
                if b == []:
                    print("Nenhuma carona disponível")
                    print("")
                    perfil(1)
                    
                if b != []:
                    m = add(j)
                    addc(m, usuario)
                    
            elif g == "volta":
                b, j = receber(g, usuario)
                print("")
                abrirl(b)
                print("")
                
                if b == []:
                    print("Nenhuma carona disponível")
                    print("")
                    perfil(1)
                    
                if b != []:
                    m = add(j)
                    addc(m, usuario)
                    
                        
            elif g != "ida" and g != "volta":
                print("Reposta inválida")
                perfil(1)

        if p == "n":

            g = ""
            b, j = receber(g, usuario)
            print("")
            abrirl(b)
            print("")
            
            if b == []:                    
                print("Nenhuma carona disponível")
                print("")
                perfil(1)
                
            if b != []:
                m = add(j)
                addc(m, usuario)

        else:
            print("Mensagem inválida!   ")
            perfil(1)

    else:
        perfil(1)

def menu2(usuario):
    
    k = pesquisa(codigo(usuario), 0)
    j = pesquisa(codigo("usuario"), 0)
    z = set(k) & set(j)
    z = list(z)

    z = int(z[0])
            
    with open("registrado.txt") as f:
        texto = f.readlines()[z]
    
    h = show(texto)

    if h == []:
        print("")
        print("Nenhuma carona foi adicionada")
        print("")
        perfil(1)

    a = show4(texto)
    abrirl(h)
            
    r = input("Deseja exluir(1) uma carona ; pegar o contato(2) ; voltar(3)?    ")

    if r == "1":
        t = input("Qual o número desejado? ")
        
        try:
            t = int(t)
        except:
            print("Número inválido! 	")
            return menu2(usuario)
        
        if t > len(h) or t == 0:
            print("Número inválido")
            return menu2(usuario)
        del a[t]
        a = LtoS(a)
        alterar_linha(z, a)
        menu2(usuario)
        
    if r == "2":
        
        t = input("Qual o número da carona desejada?    ")
        try:
            t = int(t)
        except:
            print("Número inválido! 	")
            return menu2(usuario)
        
        if t > len(h) or t == 0:
            print("Número inválido")
            return menu2(usuario)
        
        a = str(a[t])
        a = a[1:]
        a = abrir3(a)
        k = pesquisa(codigo(a), 0)
        j = pesquisa(codigo("usuario"), 0)
        z = set(k) & set(j)
        z = list(z)
        z = int(z[0])
        
        with open("registrado.txt") as f:
            texto = f.readlines()[z]
        
        texto = show4(texto)
        texto = texto[0]
        texto = texto.strip()
        texto = texto + "+"
        texto = tradutor(texto)  
        print("")      
        print(texto[4])
        menu2(usuario)

    if r == "3":
        perfil(1)

    else:
        print("Mensagem inválida!   ")
        menu2(usuario)
          
   
def add(j):
    
    y = []
    r = input("Deseja adicionar alguma carona? (s) ou (n) :   ")
    
    if r == "s":
        m = input("Qual o número da carona desejada?    ")
        try:
            m = int(m)
            y.append(j[m - 1])
        except:
            print("Número inválido! ")
            return add(j)
        return y

    elif r == "n":
        perfil(1)  

    else:
        print("Resposta inválida")
        add(j)
      
                                
def menu(usuario):
    
    z = find(usuario)
    m = find("+")
    
    for g in range(len(m)):
        if m[g] in z:
            z.remove(m[g])

    n = []
    for l in range(len(z)):
        d = z[l]
        with open("registrado.txt") as f:
            texto = f.readlines()[d]
            n.append(texto)
    
    l = show3(n)
        
    if l != []:    
        abrirl(l)
        
    if l == []:
        print("")
        print("Nenhuma carona está sendo oferecida! ")
        print("")

        o = input("Deseja adicionar(1) uma carona ou voltar(2)?   ")

        if o == "2":
            perfil(1)

        if o == "1":
            p_dar(usuario)
            menu(usuario)
            perfil(1)
        
        else:
            print("Resposta inválida!   ")
            menu(usuario)
    
    o = input("Deseja adicionar(1) uma carona, apagar uma carona(2) ou voltar(3)?   ")
   
    if o == "1":
        p_dar(usuario)
        menu(usuario)
        perfil(1)
    
    if o == "2":
        
        while True:
            try:
                h = input("Qual o número para apagar?   ")
                h = int(h)
                h = h - 1
                j = str(n[h])
                break
            except:
                print("número inválido")
        j = j.strip()
        
        with open('registrado.txt', 'r') as fr:
            lines = fr.readlines()
  
            with open('registrado.txt', 'w') as fw:
                for line in lines:
                
                    if line.strip('\n') != j:
                        fw.write(line)
        
        print("Apagado com sucesso")
        menu(usuario)
        
    if o == "3":
        perfil(1)

    else:
        print("Resposta inválida!   ")
        menu(usuario)
                            
def p_dar(x):
        
        s = input("ida ou volta?    ")
        s = s.strip()
        
        if s == "ida":
            return dar(s, x)
            
        if s == "volta":
            return dar(s, x)   
                 
        elif s != "ida" and s != "volta":
            print("Reposta inválida")
            return p_dar(x)          
            
def show(z):
    
    z = str(z)
    y = ""
    i = []
    g = []
    
    for a in z:
        
        if a == "+":
            a = ""
            g.append(y)
            y = ""
            
        y = y + a
        
    g.append(y)
    del g[0]
    del g[-1]
    
    for a in range(len(g)):
    
        i.append(abrir2(str(g[a]))) 
                      
    return i

def show3(z):
    
    a = 0
    
    while a < len(z):
        if "+" in z[a]:
            del z[a]
            a = a + 1
        a =  a + 1
        
    i = []
    
    for b in range(len(z)):
        
        i.append(str(abrir2(z[b])))
                         
    return i    
            
def show4(z):
    
    z = str(z)
    y = ""
    i = []
    g = []
    
    for a in z:
        
        if a == "+":
            g.append(y)
            y = ""
            
        y = y + a
        
    g.append(y)
    
    for a in range(len(g)):
    
        i.append(str(g[a]))
                      
    return i

def show2(z):
    
    z = str(z)
    y = ""
    i = []
    g = []
    
    for a in z:
        
        if a == "+":
            a = ""
            g.append(y)
            y = ""
            
        y = y + a
        
    g.append(y)
    del g[0]
    del g[-1]
    
    for a in range(len(g)):
    
        i.append(str(g[a]))
                      
    return i
                
def abrirl(d):
    print("")
    for a in range(len(d)):
        print(str(a + 1) + "# " + str(d[a]))
        print("")
      
def LtoS(a):
    y = ""
    for b in range(len(a)):
        y = y + a[b]
        
    return y

def abrir3(f):
    
    f = str(f)
    x = []
    y = ""
    
    for a in f:
        if a == "-":
            a = ""
            x.append(y)
            y = ""
        y = y + a
    x.append(y)
    
    user = str(x[0])

    return user

def relogio():

    caronas = find("volta") + find("ida")

    linhas = []
    for l in range(len(caronas)):
        d = caronas[l]
        with open("registrado.txt") as f:
            texto = f.readlines()[d]
            linhas.append(texto)

    datas = []
    for a in linhas:
        a = a.split("-")
        if "+" not in a[5]:
            datas.append(a[5].strip())

    return datas

def atual():

    datas = relogio()
    tempo = datetime.now()
    diaAtual = tempo.day
    mesAtual = tempo.month

    z = len(datas)
    a = 0
    while a < z:
        x = datas[a].split("/")
        mes = int(x[1])

        if mes > mesAtual:
            del datas[a]
            z = z - 1
            a = a - 1

        a = a + 1
     
    a = 0    
    while a < z:
        x = datas[a].split("/")
        dia = int(x[0])
        mes = int(x[1])

        if mes == mesAtual and dia >= diaAtual:
            del datas[a]
            z = z - 1
            a = a - 1
        a = a + 1
    
    caronas = pesquisa(datas, "sdfdfs")
    
    linhas = []
    for l in range(len(caronas)):
        d = caronas[l]
        with open("registrado.txt") as f:
            texto = f.readlines()[d]
            linhas.append(texto)    
    
    novaslinhas = []
    
    for b in linhas:
        if "+" in b:
            b = b.strip()
            k = b.split("+")
            h = k
            for g in k:
                for t in datas:
                    if t in g:
                        h.remove(g)
            m = ""
            for j in h:
                m = m + j + "+"
                
            m = m[:-1]
            h = m
                
        else:
            h = ""
        
        novaslinhas.append(h)
    
    for c in range(len(novaslinhas)):
        
        alterar_linha(caronas[c], novaslinhas[c])        

perfil(0)
