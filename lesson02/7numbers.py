i=1
k=0
while True:
    
    if i%2==0 and i%10 + (i-i//100*100)//10 + i//100==9:
        print (i)
        k+=1
    i+=1
    if k==7:break
