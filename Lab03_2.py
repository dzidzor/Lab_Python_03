


#Lab03_2a
for n in range (0,7):
    for m in range(1,n+1,1):
        print m,
    print""

    
print""    

#Lab03_2b
for n in range (7,0,-1):
    for m in range(1,n,1):
        print m,
    print""
print""

#Lab03_2c
for n in range (1,7,1):
    for m in range (7-n,1,-1):
        print "",
    for p in range(n,0,-1):
        print p,
    print""
    
    
#Lab03_2d
for n in range (7,0,-1):
    for m in range (7-n,0,-1):
        print "",
    for p in range(1,n,1):
        print p,
    print""
        

#Lab03_2e
for n in range (1,7,1):
    for m in range (7-n,1,-1):
        print "",
    for p in range(n-1,0,-1):
        print p,
    for q in range(2,n,1):
        print q,
    print""
        
