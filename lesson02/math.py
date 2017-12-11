#求1+2+3+。。。+100
s = 0
for i in range(1,101):
    s+=i
print(s)

#求2+4+6+。。。+100
s = 0
for i in range(1,101):
    if i%2==0:
        s+=i
print(s)

#求1+3+5+。。。+100
s = 0
for i in range(1,101):
    if i%2!=0:
        s+=i
print(s)

#求1+3+5+。。。+100
s = 0
for i in range(1,101):
    if i%2!=0:continue
    s+=i
print(s)

#0-100中，偶数且各个数位相加=9
for i in range(1,101):
    if i%2==0 and i%10 + i//10==9:
        print (i)

for i in range(1,101):
    if i%2!=0:continue
    if i%10 + i//10==9:
        print (i)
        
#输出偶数且各个数位相加=9（7个）
i=1
k=0
while True:
    
    if i%2==0 and i%10 + (i-i//100*100)//10 + i//100==9:
        print (i)
        k+=1
    i+=1
    if k==7:break
    
