from datetime import date, datetime
from carona import find, pesquisa

def alterar_linha(index_linha,nova_linha):
    
    with open('registrado.txt','r') as f:
        texto = f.readlines()
    with open('registrado.txt','w') as f:
        for i in texto:
            if texto.index(i)==index_linha:
                f.write(nova_linha + '\n')
            else:
                f.write(i)
                
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
        
          
    
    

    
atual()