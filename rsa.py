import math
import random
def issimple(a):
    if a%2==0:
        return False
    for i in range(3,a,2):
        if a%i==0:
            return False
    return True

p=random.randint(3,1024)
while not issimple(p):
    p = random.randint(3, 1024)

q=random.randint(3,1024)
while not issimple(q):
    q = random.randint(3, 1024)

print('p = ',p,'q = ',q)
n=p*q
print('n = ',n)
fi=(p-1)*(q-1)
print('fi = ',fi)

e=random.randint(3,fi)
while not issimple(e):
   if  math.gcd(e,fi)==1 and issimple(e):
       break
   else:e=random.randint(3,fi)
print('e = ',e)

for d in range(fi):
    if e*d%fi==1:
        break
print('d = ',d)
print('введите сообщение')
mess=input()
c=[]
for alpha in mess:
    c.append((ord(alpha)**e)%n)
for el in c:
    print(el,end='')
print()
de_mess=""
for alpha in c:
    de_mess+=chr((alpha**d)%n)
print(de_mess)








