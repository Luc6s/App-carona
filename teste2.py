a = [1, 2, 4]

e = [1, 4, 5]

f =  set(a) & set(e)

f = list(f)
print(f)

k = a

for b in a:    
    if b in f:
        k.remove(b)   
            
print(k)
