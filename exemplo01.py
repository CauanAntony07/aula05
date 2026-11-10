valor_ped = float(input('digite o valor: '))
distancia = float(input('distancia: '))
frete = 8

if valor_ped > 50 and distancia <= 3:
    valor_final = valor_ped 
    print(f'frete gratis')

else:
    valor_final = valor_ped + 8
    print(f'frete de {frete}')
    print(f'valor final: R$ {valor_final:.2f}')