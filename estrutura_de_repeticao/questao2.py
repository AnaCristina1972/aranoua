'''2.Crie  um programaque  leia  um  número  inteiro  e  positivo  e  verifique  se  ele  é  primo  ou  não.  
(Dica:  os números primos são os números que só podem ser divididos por eles mesmos e por 1).'''
from numpy import *
primo=int(input("digite um valor: "))
#primo+=1
primo1=False
if primo>1 :
    primo1=True
   
    for i in range(2,int(primo**0.5)+1):
        print(f"i: ",i)
        if(primo%i==0):         
           primo1=False
           print(f"O numero {primo} não é primo...  ")
if primo1:
    print(f"O numero {primo} é primo***** ")

                  
else: print(f"O numero {primo} não é primo ")



