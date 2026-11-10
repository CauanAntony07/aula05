compras = float(input('digite o valor da sua compra: '))
cliente = input(f'voce e cadastrado no programa fidelidade? [s/n]').lower()[0]

frete = 25

if compras > 200 or cliente == 's':
    print(f'O valor da sua compra deu: {compras:.2f}')
    print('voce gahou frete gratis!!!')

else:
    valor_fi = compras + frete
    print(f'O valor da sua compra deu: {valor_fi}')
