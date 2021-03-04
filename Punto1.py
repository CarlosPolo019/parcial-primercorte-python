numLlantas = float(input('Digite la cantidad de llantas Ponchadas quiere comprar: '))
if numLlantas > 0:
    if numLlantas < 5:
        valorLlanta = 300
        valorCompra =  numLlantas * valorLlanta
    elif (numLlantas >= 5) and (numLlantas <= 10):
        valorLlanta = 250
        valorCompra =  numLlantas * valorLlanta
    else:
        valorLlanta = 200
        valorCompra =  numLlantas * valorLlanta
    print(f'Valor de cada llanta marca Ponchadas: {valorLlanta}')
    print(f'Valor de la compra: {valorCompra}')
else:
    print(f'El valor ingresado debe ser mayor a 0')
