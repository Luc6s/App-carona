def abrir2(f):
    
    f = str(f)
    x = []
    y = ""
    
    x = f.split("-")
    
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
    origens = origens.title()
    bairros = bairros.title()
    dia = dia.strip()
    
    u = user + " / " + via + " / " + dia + " / " + origens +  " / " + h1 + " até " + h2 +  " / " + bairros
    
    if h1 == "Qualquer Hora 1" and h2 == "Qualquer Hora 2":
        u = user + " / " + via + " / " + dia + " / " + origens +  " / " + "Qualquer Hora" + " / " + bairros
        
    return u

a = abrir2('lucas-volta-Qualquer Origem-Qualquer Hora 1 / NT / Qualquer Hora 2-Qualquer Destino-10/03\n')

print(a)