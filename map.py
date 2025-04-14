# Desafio 1
# Usando a lista compreheension, crie a seguinte lista:
[2, 4, 6, 8, 10]


pares1 = [2 * i for i in range (1,6)]
print(pares1)

print([i for i in range(0,11) if i not in (0,1,3,5,7,9)])

def imprimir_apenas_pares(numero):
    if numero == 0:
        return False
    valor = numero % 2
    if valor == 0:
        return True
    else:
        return False
    
print([i for i in range(11) if imprimir_apenas_pares(i)])

# Desafio 2
# Use a seguinte lista como base:
cores = ['vermelho','azul','verde','amarelo','rosa','preto']

# Para criar a lista a seguir:
['1 - vermelho','2 - azul','3 - verde','4 - amarelo','5 - rosa','6 - preto']

def numerar_cores(indice_cor):
    i, cor = indice_cor
    return f"{i + 1} - {cor}"
    
print(list(map(numerar_cores, enumerate(cores))))  

# Desafio 3 
# Usando a lista a seguir como base:
participantes = ['joel','jessica','maria','cris','Larissa','rafael','marcus','john']
pagamento_realizado = ['joel','jessica','maria','cris']
'''
Concatene(adicione) a palavra 'PAGO' aos nomes da lista 'participantes' usando condicionais somente nos casos onde seu nome esteja na lista 'pagamento_realizado'. O resultado final deve ser como a lista a seguir:
'''
['joael PAGO','jessica PAGO','maria PAGO','cris PAGO','Larissa','rafael','marcus','john']

print([f"{i} PAGO" if i in pagamento_realizado else i for i in participantes])



