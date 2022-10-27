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
    
    
def tempo1(x):
    
    if x == 0:
        a = input("Algum horário de preferência? (s) ou (n) :    ")
    else:
        a = "s"
        
    if a == "s":
        hora = input("Hora(apenas de 5 em 5 min): hr:mn :   ")
        hora = hora.strip()
        if hora == "":
            print("Hora inválida")
            tempo1(1)
        return hora
    else:
        return "Qualquer Hora 1"
    
def tempo2():
    
        k = input("Deseja um período de tempo? (s) ou (n)  ")
        if k == "s":
            hora = input("Até(apenas de 5 em 5 min): hr:mn :   ")
            hora = hora.strip()
            if hora == "":
                hora = "Qualquer Hora 2"
        if k == "n":
            return 90
        
        else:
            print("Resposta Inválida!   ")
            return tempo2()
        
        return hora
    
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
        if b != 0:
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

def periododia(dia1):
    
    p = input("Deseja um período de data? (s) ou (n)  ")

    if p == "s":
        while True:
            try:
                dia2 = data()
                formatodata(dia2)
                break
            except:
                print("Formato inserido incorreto!  ")
        
        d1, m1 = dia1.split("/")
        d2, m2 = dia2.split("/")
        d1 = int(d1)
        m1 = int(m1)
        d2 = int(d2)
        m2 = int(m2)
        data3 = []
        while m1 < m2:
            a = data_valida(d1, m1)
            
            if a == 0:
                d1 = 0
                m1 = m1 + 1
                
            d1 = d1 + 1
               
def receber(s, y):

    via = s

    w = input("Deseja alguma data como filtro? (s) ou (n) :   ")
    w = w.strip()

    if w == "s":
        while True:
            try:
                dia = data()
                formatodata(dia)
                break
            except:
                print("Formato inserido incorreto!  ")
        periodo = periododia(dia)
            
    if w == "n":
        dia = ""

    else:
        return receber(s, y) 

    x = 0
    hora1 = tempo1(0)
    
    if hora1 != "Qualquer Hora 1":
        hora2 = tempo2()
        if hora2 == 90:
            hora2 = hora1
        
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
    
    if via == "":
        u = pesquisa("volta", 0)
        i = pesquisa("ida", 0)
        h = u + i
    else:
        h = pesquisa(via, 0)
        
    q = pesquisa(dia, 0)
    j = pesquisa(hora1, "Qualquer Hora 1")
    g = pesquisa(origem, "Qualquer Origem")
    v = pesquisa(hora2, "Qualquer Hora 2")
    b = pesquisa(bairro, "Qualquer Destino")
    k = pesquisa(y, 0)
    c = pesquisa(codigo(y), 0)
    e = find("+")
    z = (set(h) & set(j) & set(g) & set(b) & set(v) & set(q))
    z = list(z)
    
    m = k + c + e
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
    
    x = f.split("-")
    
    horas = str(x[3])
    
    horas = horas.split("/")
    h1 = horas[0]
    h2 = horas[-1]
            
    h2 = h2.strip()
    h1 = h1.strip()
    user = str(x[0])
    via = str(x[1])
    via = via.title()
    origens = str(x[2])
    bairros = str(x[4])
    dia = str(x[5])
    
    bairro1 = ""
    bairro2 = ""
    bairro3 = ""

    t = len(bairros.split("_"))

    if t == 3:
        bairro1, bairro2, bairro3 = bairros.split("_")
        
    if t == 2:
        bairro1, bairro2 = bairros.split("_")
        
    if t == 1:
        bairro1 = bairros
        
    bairros = bairro1 + " " + bairro2 + " " + bairro3
    
    origem1 = ""
    origem2 = ""
    origem3 = ""

    t = len(origens.split("_"))

    if t == 3:
        origem1, origem2, origem3 = origens.split("_")
        
    if t == 2:
        origem1, origem2 = origens.split("_")
        
    if t == 1:
        origem1 = origens
        
    origens = origem1 + " " + origem2 + " " + origem3
    
    origens = origens.strip()
    bairros = bairros.strip()
    origens = origens.title()
    bairros = bairros.title()
    dia = dia.strip()
    
    if via == "Volta" and origens == "Qualquer Origem":
        origens = "Qualquer Campus"    
    
    if via == "Ida" and bairros == "Qualquer Destino":
        bairros = "Qualquer Campus"
        
    u = user + " / " + via + " / " + dia + " / " + origens +  " / " + h1 + " até " + h2 +  " / " + bairros
    
    if h1 == "Qualquer Hora 1" and h2 == "Qualquer Hora 2":
        u = user + " / " + via + " / " + dia + " / " + origens +  " / " + "Qualquer Hora" + " / " + bairros
    
    if h1 == h2:
        u = user + " / " + via + " / " + dia + " / " + origens +  " / " + h1 +  " / " + bairros
    
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
        
    hora1 = tempo1(0)

    if hora1 != "Qualquer Hora 1":
        hora2 = tempo2()
        
        if hora2 == 90:
            hora2 = hora1

    else: 
        hora2 = "Qualquer Hora 2"

    if hora1 != "Qualquer Hora 1" and hora2 != "Qualquer Hora 2":
        while True:
            try:
                entre = formatohora(hora1, hora2)
                break

            except:
                print("Formato de hora inserido incorreto!  ")
                hora1 = tempo1(1)
                hora2 = tempo2()
    else:
        entre = "NT"  
        
    while True:            
        try:            
            origem = lugar(0)
            if via == "ida" and origem == "Qualquer Origem":
                int("a")
            break
        except:
            print("Adicione pelo menos uma origem!  ")
    
    if origem != "Qualquer Origem":
        while x < 2:
            
            r = input("Deseja adicionar outra origem(limite de 3)? (s) ou (n):  ")
            if r == "s":
                origem = origem + "_" + lugar(1)
                x = x + 1
            if r == "n":
                x = 10
                
    while True:            
        try:            
            bairro = destino(0)
            if via == "volta" and bairro == "Qualquer Destino":
                int("a")
            break
        except:
            print("Adicione pelo menos um destino!  ")
    
    x = 0
    if bairro != "Qualquer Destino":
        while x < 2:
            
            r = input("Deseja adicionar outro destino(limite de 3)? (s) ou (n):  ")
            if r == "s":
                bairro = bairro + "_" + destino(1)
                x = x + 1
            if r == "n":
                x = 10
        
    caminho = ("\n" + user + "-" + via + "-" + origem + "-" + hora1 + " / " + entre + " / " + hora2 + "-" + bairro + "-" + d)
        
    tela = (user + "-" + via + "-" + origem + "-" + hora1 + " / " + entre + " / " + hora2 + "-" + bairro + "-" + d)
    arq2 = open('registrado.txt', 'r')
    p = okay() 
    
    if p == 0:
        return caminho

    if tela not in arq2 and p == 1:
        arq2.close()
        arq2 = open('registrado.txt', 'a')
        arq2.write(caminho)
    
    else:
        print("Carona já existente! ")
        return caminho
    
    print("")
    print(abrir2(tela))
    print("")
    
    arq2.close()
    print("Carona adicionada com sucesso! ")
    
    return caminho
    
def validarhora(f):
    
    if len(f) > 5:
        return int("a")
    
    h = ""
    m = ""
    h, m = f.split(":")
    k = ["00", "05", "10", "15", "20", '25', '30', '35', "40", '45', '50', '55']
 
    if str(m) not in k:
        return int("a")
            
    h = int(h)
    m = int(m)
    
    if h > 24:
        return int("a")
    
    else:
        return h, m

def data_valida(d, m):
    
    if d > 31:
        return 0
    
    if m > 12:
        return 0
    
    t = [4, 6, 9, 11]
    
    for b in range(len(t)):
        
        if d > 30 and m == t[b]:
            return 0
        
    h = [1, 3, 5, 7, 8, 10, 12]
    
    for n in range(len(h)):
        
        if d > 31 and m == h[n]:
            return 0
        
    if d > 29 and m == 2:
        return 0
    
    else:
        return 1
    
def formatodata(f):
    if len(f) != 5:
        int("a")
    d = ""
    m = ""
    y = 0
    
    d, m = f.split("/")
        
    d = int(d)
    m = int(m)
    if m > 12:
        int("a")
    
    h = data_valida(d, m)
    
    if h:
        m = str(m)
        d = str(d)
        g = d + "/" + m
        return g
    
    else:
        int("a")
        
def formatohora(t1, t2):
    h1, m1 = validarhora(t1)
    h2, m2 = validarhora(t2)
    x = []
    y = ""
    
    if h1 == h2 and m1 == m2:
        return "NT"
    
    if h1 != h2:
        
        while h1 < h2:
            m1 = m1 + 5
            if m1 == 60:
                h1 = h1 + 1
                m1 = "00"
            if m1 == 5:
                m1 = "05"
            x.append(str(h1) + ":" + str(m1))
            m1 = int(m1)
 
    if h1 == h2:
    
        while m1 < int(m2):
            m1 = m1 + 5
            if m1 == 5:
                m1 = "05"
            x.append(str(h1) + ":" + str(m1))
            m1 = int(m1)
               
    for a in range(len(x)):
        if x[a] == x[-1]:
            break
        y = y + str(x[a]) + " / "
        
    y = y.strip()
    y = y[:-1]
    y = y.strip()

    return y
        
def okay():
    
    r = input("Confirma? (s) ou (n):    ")
    
    if r == "s":
        return 1
    
    if r == "n":
        return 0

    else:
        print("Respota inválida!    ")
        return okay()
    
    
arq2.close()

