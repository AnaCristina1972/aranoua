'''3.Construa um algoritmo que leia 5 números inteiros e escreva os números em ordem crescente. 
(Dica: pesquisar método de Ordenação Bolha)'''

numbers = [7, 3, 6, 2, 0]
size = len(numbers)
for i in range(size -1): 
    for j in range (size -1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]