num = float(input('digite um numero: '))

match num:
    case 0:
        print("zero")
    case n if n > 0:
        print("positivo")
    case n if n < 0:
        print("negativo")
