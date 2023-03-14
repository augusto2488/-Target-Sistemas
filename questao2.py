import math
 

def ehQuadradoPerfeito(x):
    s = int(math.sqrt(x))
    return s*s == x
 

def ehFibonacci(n):
 
    return ehQuadradoPerfeito(5*n*n + 4) or ehQuadradoPerfeito(5*n*n - 4)
  

for i in range(1,11):
     if (ehFibonacci(i) == True):
         print (i,"Faz parte da sequencia Fibonacci")
     else:
         print (i,"Não faz parte da sequencia Fibonacci")
         
