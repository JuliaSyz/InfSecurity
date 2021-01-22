import random
def issimple(a):
    if a%2==0:
        return False
    for i in range(3,a,2):
        if a%i==0:
            return False
    return True




p=int(input())
q=int(input())

a = random.randint(3, 1024)
while not issimple(a):
    a = random.randint(3, 1024)

b = random.randint(3, 1024)
while not issimple(b):
    b = random.randint(3, 1024)

a=int(input())
b=int(input())
A=round(q**a%p,0)
B=round(p**b%q,0)

S_A=round(B**a%p,0)
S_B=round(A**b%p,0)

if S_A==S_B:
    print('yes',S_A)
else:print('no')











