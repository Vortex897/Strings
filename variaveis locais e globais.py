import os
def limpa():
    os.system('cls')
limpa()

def f1(a):
    print(a+x)
    
def f2(a):
    c = 10 #variavel local, pois foi declarada dentro
    print(a+x+c)
    
def f3(a):
    global x #deixar claro que esta sendo usado um x global
    x = x + 1
    print(a+x)
    
def f4(a):
    global c
    c = 10
    print('x from f4;', c)
    print(a+x+c)
    
    
x = 4   #variavel global pois foi declarada fora das funções

f1(3)
f2(3)
print(x)


x = 4   #x global
f1(3)
#f3(3) #da erro se tiver um x local dentro da função
print(x)



x = 4
f1(3)
f3(3)
print(x)


    
x=4
f2(3)
print(x)
#print(c)



x = 4
c = -1
f4(1)
print('c global:', c)