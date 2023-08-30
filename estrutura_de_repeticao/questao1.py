'''Em uma determinada escola, 3 candidatos (D, G, X) concorrem ao cargo de Diretor Geral. A urna
eletrônica elaborada para essa eleição, aceita os votos conforme a legenda abaixo:'''

from numpy import *
cont=zeros(5,dtype=int)
vencedor=""
voto=[]
pessoas=0
validos=0
candidatos=["D","G","X","EM BRANCOS","NULOS"]
print("“A” Candidato D\n“B” Candidato G\n“C” Candidato X\n“O” Voto em Branco\n“N” Voto Nulo\n“F” Finaliza a eleição\n")
voto=input("Qual é seu candidato?").upper().split(',')
for i in range(size(voto)): 
    if(voto[i]!="F"):  
        pessoas+=1
        if(voto[i]=='A'):
            cont[0]+=1
            validos+=1
        elif(voto[i]=="B"):
            cont[1]+=1
            validos+=1

        elif(voto[i]=="C"):
            cont[2]+=1
            validos+=1
        elif(voto[i]=="O"):cont[3]+=1
        elif(voto[i]=="N"):cont[4]+=1
        else:print("Opção invalida")
    else:   
        break
print("")
for i in range(size(cont)):
    print(f"Candidato {candidatos[i]} teve {cont[i]} votos")
    if cont[i]==max(cont):
        vencedor=candidatos[i]
print("\nCandidato",vencedor," será o Diretor geral, pois  teve ",max(cont)," votos")
print("Votos validos: ",validos)
print("Total de eleitores: ",pessoas)
      




