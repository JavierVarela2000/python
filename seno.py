i=0
s=0
c=1
c1=1
b=3
f=3
r=0
d=1
e=1
x=float(input("valor a calcular"))
r=r+x
for i in range(3):
    
    if(i%2==0):
        s=-1
    else:
        s=1
  
    while(b>=c1):
        d=d*x
        c1=c1+1
    b=b+2
    while(f>=c):
 
        e=e*c
        c=c+1
  
    f=f+2
    r=r+(s*d/e)

print(r)   
    

