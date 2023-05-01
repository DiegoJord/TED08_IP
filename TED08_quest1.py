# Faça um algoritmo para ler 20 números e armazenar em um vetor. Após a leitura total dos 20
# números, o algoritmo deve escrever esses 20 números lidos na ordem inversa.

num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for i in range (0,21):
    num1.sort(reverse=True)
print(num1)
