from login import *

arq2 = open('registrado.txt', 'a')
  
def data():
    a = input("Qual o dia da carona? dd/mm :   ")
    a = a.strip()
    return a
    
def lugar(x):
    
    if x == 0:
        a = input("Alguma origem de preferência? (s) ou (n) :   ")
        
    else:
        a = "s"
        
    if a == "s":
        bairro = input("Origem: ")
        bairro = bairro.strip()
        
        if bairro == "":
            print("Origem inválida")
            lugar()
            
        return bairro.lower()
        
    else:
        return "Qualquer Origem"
    
    
def tempo1():
    a = input("Algum horário de preferência? (s) ou (n) :    ")
    if a == "s":
        hora = input("Hora(apenas de 20 em 20 min): hr:mn :   ")
        hora = hora.strip()
        if hora == "":
            print("Hora inválida")
            tempo1()
        return hora.lower()
    else:
        return "Qualquer Hora 1"
    
def tempo2():
        hora = input("Até(apenas de 20 em 20 min): hr:mn :   ")
        hora = hora.strip()
        if hora == "":
            hora = "Qualquer Hora 2"
        return hora.lower()
    
def destino(x):
    if x == 0:
        a = input("Algum destino de preferência? (s) ou (n) :    ")
    else:
        a = "s"
    if a == "s":
        bairro = input("Destino: ")
        bairro = bairro.strip()
        if bairro == "":    
            print("Destino inválida")
            destino()
        return bairro.lower()
    else:
        return "Qualquer Destino"
    
def pesquisa(a, b):

    if type(a) != list:
        x = []
        x = find(a)
        
        if b == 0:
            pass
        
        else:
            x = x + find(b)
        
        return x
    
    if type(a) == list:
        y = []
        y = find(b)
        
        for t in range(len(a)):
            l = find(a[t])
            
            y = y + l
       
        return y
    
def find(a):
    x = []
    with open("registrado.txt", 'r') as fp:

        lines = fp.readlines()
        
        for line in lines:

            if line.find(a) != -1:
                x.append(lines.index(line))           
    return x
    
def inicio2(x):    
    r = input("Quer dar(1) ; receber(2) carona ; acessar perfil(3) ; sair(4)?   ")
    r = r.strip()
    
    if r == "1":
        
        s = input("ida ou volta?    ")
        s = s.strip()
        
        if s == "ida":
            return dar(s, x)
            
        if s == "volta":
            return dar(s, x)
        
                 
        elif s != "ida" and s != "volta":
            print("Reposta inválida")
            return inicio2(x)  
            
    elif r == "2":
        return "2"
    
    elif r == "3":
        return "3"
    
    elif r == "4":
        return 10
    
    elif r != "2" and r != "1":
        print("Resposta inválida")
        return inicio2(x)
   
def receber(s, y):
    via = s
    x = 0
    hora1 = tempo1()
    
    if hora1 != "Qualquer Hora 1":
        hora2 = tempo2()
        
    else: hora2 = "Qualquer Hora 2"
    
    if hora1 == "Qualquer Hora 1":
        hora1 = ""
        hora2 = ""
        
    if hora2 == "Qualquer Hora 2":
        hora2 = ""
    origem = []
    origem.append(lugar(0))
        
    if origem[0] != "Qualquer Origem":
        while x < 2:
            
            r = input("Deseja adicionar outra origem(limite de 3)? (s) ou (n):  ")
            if r == "s":
                origem.append(lugar(1))
                x = x + 1
            if r == "n":
                x = 10
    else:
        origem = ""
    
    bairro = []
    bairro.append(destino(0))
    x = 0
    
    if bairro[0] != "Qualquer Destino":
        while x < 2:
            
            r = input("Deseja adicionar outro destino(limite de 3)? (s) ou (n):  ")
            if r == "s":
                bairro.append(destino(1))
                x = x + 1
            if r == "n":
                x = 10
    else:
        bairro = ""
        
    if bairro == "Qualquer Destino":
        bairro = ""
        
    h = pesquisa(via, 0)
    j = pesquisa(hora1, "Qualquer Hora 1")
    g = pesquisa(origem, "Qualquer Origem")
    v = pesquisa(hora2, "Qualquer Hora 2")
    b = pesquisa(bairro, "Qualquer Destino")
    k = pesquisa(y, 0)
    c = pesquisa(codigo(y), 0)
    z = (set(h) & set(j) & set(g) & set(b) & set(v))
    z = list(z)
    
    m = k + c
    for a in range(len(m)):
        if m[a] in z:
            z.remove(m[a])
               
    t = 0
    l = []
    o = []
    
    while t < len(z):
        n = int(z[t])
        arquivo = open("registrado.txt")     
        f = arquivo.readlines()
        d = (f[n])
        l.append(abrir2(d))       
        o.append(d)
        arquivo.close()
        t = t + 1
    
    
        
    return l, o	
     
def abrir2(f):
    
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
    horas = str(x[3])
    i = 0
    h = ""
    
    for b in horas:
        
        if b == "/" and i == 0:
            i = 1
            h1 = h
            
        if b == "/":
            h = ""    
        h = h + b 
        
    h2 = h.strip() 
    h2 = h2[1:]   
    h2 = h2.strip()
    h1 = h1.strip()
    user = str(x[0])
    via = str(x[1])
    origens = str(x[2])
    bairros = str(x[4])
    u = user + " / " + via + " / " + origens +  " / " + h1 + " até " + h2 +  " / " + bairros
    
    if h1 == "Qualquer Hora 1" and h2 == "Qualquer Hora 2":
        u = user + " / " + via + " / " + origens +  " / " + "Qualquer Hora" + " / " + bairros
        
    return u


def dar(s, h):

    while True:
        try:
            d = data()
            formatodata(d)
            break
        except:
            print("Formato inserido incorreto!  ")

    user = str(h)
    x = 0
    via = s
    hora1 = tempo1()

    if hora1 != "Qualquer Hora 1":
        hora2 = tempo2()

    else: 
        hora2 = "Qualquer Hora 2"

    if hora1 != "Qualquer Hora 1" and hora2 != "Qualquer Hora 2":
        while True:
            try:
                entre = periodo(hora1, hora2)
                break

            except:
                print("Formato de hora inserido incorreto!  ")

    origem = lugar(0)
    
    if origem != "Qualquer Origem":
        while x < 2:
            
            r = input("Deseja adicionar outra origem(limite de 3)? (s) ou (n):  ")
            if r == "s":
                origem = origem + " " + lugar(1)
                x = x + 1
            if r == "n":
                x = 10
                
    bairro = destino(0)
    x = 0
    if bairro != "Qualquer Destino":
        while x < 2:
            
            r = input("Deseja adicionar outro destino(limite de 3)? (s) ou (n):  ")
            if r == "s":
                bairro = bairro + " " + destino(1)
                x = x + 1
            if r == "n":
                x = 10
        
    else:
        entre = "NT"
        
    caminho = ("\n" + user + "-" + via + "-" + origem + "-" + hora1 + " / " + entre + " / " + hora2 + "-" + bairro)
    
    if hora1 == "Qualquer Hora 1":
        horas = "Qualquer horário"
        
    else: 
        horas = hora1 + " até " + hora2
        
    tela = (user + "-" + via + "-" + origem + "-" + hora1 + " / " + entre + " / " + hora2 + "-" + bairro)
    arq2 = open('registrado.txt', 'r')
    p = okay() 

    if tela not in arq2 and p == 1:
        arq2.close()
        arq2 = open('registrado.txt', 'a')
        arq2.write(caminho)
    
    elif p == 0:
        return caminho
    
    else:
        print("Carona já existente! ")
        return caminho
        
    arq2.close()
    print("Carona adicionada com sucesso! ")
    
    return caminho
    
def formato(f):
    h = ""
    m = ""
    y = 0
    for a in f:
        if y >= 1:
            m = m + a
        if a == ":":
            y = 1
        if y == 0:
            h = h + a
    h = int(h)
    m = int(m)
    return h, m

def formatodata(f):
    if len(f) > 5:
        int("a")
    h = ""
    m = ""
    y = 0
    for a in f:
        if y >= 1:
            m = m + a
        if a == "/":
            y = 1
        if y == 0:
            h = h + a
    h = int(h)
    m = int(m)
    if m > 12:
        int("a")
    

    m = str(m)
    h = str(h)
    d = h + ":" + m
    return d
        
def periodo(t1, t2):
    h1, m1 = formato(t1)
    h2, m2 = formato(t2)
    x = []
    y = ""
    
    if h1 != h2:
        
        while h1 < h2:
            m1 = m1 + 20
            if m1 == 60:
                h1 = h1 + 1
                m1 = "00"
            x.append(str(h1) + ":" + str(m1))
            m1 = int(m1)
            
    if h1 == h2:
    
        while m1 < m2 - 20:
            m1 = m1 + 20
            x.append(str(h1) + ":" + str(m1))
            
        
    for a in range(len(x)):
        if x[a] == x[-1]:
            y = y + str(x[a])
            break
        y = y + str(x[a]) + " / "
     
    return y
        
def okay():
    
    r = input("Confirma? (s) ou (n):    ")
    
    if r == "s":
        return 1
    
    if r == "n":
        return 0
    
    
arq2.close()

