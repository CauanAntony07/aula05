print('''
[1] - sul
[2]- norte
[3] - leste
[4]- oeste
[5 a 6] - nordeste
[7 a 9] - sudeste
[10] - centro-oeste
[11] - noroeste
''')

opcao = int(input('escolha uma opcao: '))

match opcao:
    case 1:
        print('sul')
    case 2:
        print('norte')
    case 3:
        print('leste')
    case 4:
        print('oeste')
    case 5 | 6:
        print('nordesde')
    case 7 | 8 | 9:
        print('sudeste')
    case 10:
        print('centro-oeste')
    case 11:
        print('noroeste')
    case _:
        print('importado')