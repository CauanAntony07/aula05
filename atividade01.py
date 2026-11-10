not_01 = float(input('digite sua nota: '))
not_02 = float(input('digite sua nota: '))
not_03 = float(input('digite sua nota: '))
not_04 = float(input('digite sua nota: '))

media = (not_01 + not_02 + not_03 + not_04) / 4

if media >= 7:
    print(f'aprovado')

elif media >= 5 and media < 7:
    print(f'em recuperação.')

else:
    print(f'Reprovado')

    
 
