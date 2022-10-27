from datetime import date, datetime
from carona import find, abrir2


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

    print(datas)


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
        
    while a < z:
        x = datas[a].split("/")
        dia = int(x[0])
        mes = int(x[1])

        if mes == mesAtual and dia > diaAtual:
            del datas[a]
            z = z - 1
            a = a - 1
        a = a + 1
    
    print(datas)
    print (diaAtual)

    
atual()