# Script chat 
import os

mensagens = []

nome = input('Nome: ')

while True:
    
    # Limpando o terminal
    os.system('cls')
    
    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])
            
    print('_________________________')  
    
    # Obtendo o texto
    texto = input('mensagem: ')
    if texto == 'fim':
        break
    
    # Adicionando mensagem na lista
    mensagens.append({
        'nome': nome,
        'texto': texto
    })      