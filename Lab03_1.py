number=2
factor=0
counter=0
divisor=1
for counter in range(0,50):
    while number>0:
        for divisor in range(1,int(number**0.5)):
                 if number%divisor==0:
                    factor+=1
                    if factor>1:
                        break
                    elif factor==1:
                        print number
    counter+=1
                       
    

