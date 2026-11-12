valor = float(input('digite o valor da venda R$: '))

match valor:
    case v if v < 100:
        print("venda pequena")
    case v if v < 500:
        print("venda media")
    case _:
        print("venda grande")