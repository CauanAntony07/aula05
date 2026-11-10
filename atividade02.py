not_final = float(input('digite sua nota: '))
frequencia = float(input('informe sua frequencia: '))
mensalidade = float(input('qual o valor da mensalidade:?'))

desconto = mensalidade * 0.20
valor_fi = desconto - mensalidade

if not_final >= 7 and frequencia >= 75:
    print('voce tem direito a bolsa de 20%.')
    print(f'sua mensalidade é: {valor_fi}')

else:
    print('voce nao tem direito a bolsa')
    print(f'sua mensalidade é: {mensalidade}')
