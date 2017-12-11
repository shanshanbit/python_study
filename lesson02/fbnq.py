m=1
n=1
print('斐波那契数列的第 1 项是',m)
print('斐波那契数列的第 2 项是',n)
for i in range(3,101):
    k=m+n
    print('斐波那契数列的第',i,'项是',k)

    m=n
    n=k
    
    if i==100:
        l=m/n
        print('斐波那契数列的第99项和第100项的比值是',l)
        break
