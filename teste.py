def codigo(u):
    id = []  
    for letra in u:
        x = ord(letra) - 28
        id.append(str(x))
    
    id = "".join(id)
    return id

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

g = codigo("21323 ")
print(g)
g = tradutor(g)
print(g)
