# Faça um algoritmo para ler 10 números e armazenar em um vetor VET, verificar e escrever se existem
# números repetidos no vetor VET e em que posições se encontram.

diego = []
for i in range(10):
    numero = int(input(f'digite o {i+1}° número: '))
    diego.append(numero)

repetidos = []
for i in range(len(diego)):
    for j in range(i+1, len(diego)):
        if diego[i] == diego[j]:
            if diego[i] not in repetidos:
                repetidos.append(diego[i])
            print(f'O número {diego[i]} está nas posições {i+1} e {j+1}')

if len(repetidos) > 0:
    print('Os seguintes números estão repetidos:')
    print(repetidos)
else:
    print('Não foram encontrados números repetidos')