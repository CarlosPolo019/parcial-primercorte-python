numColchones = float(input('Digite la cantidad de colchones a comprar: '))
valorCholchones = float(input('Digite el valor de cada colchon: '))
if numColchones > 0:
    if valorCholchones > 0:
        if numColchones < 3:
            valorCompra =  numColchones * valorCholchones
            print(f'Valor de la compra: {valorCompra}')
        elif (numColchones >= 3) and (numColchones < 6):
            valorCompra =  numColchones * valorCholchones
            descuento = (0.20 * valorCompra)
            total = valorCompra - descuento
            print(f'Se le aplicara un descuento del: 20%')
            print(f'Valor de la compra sin descuento: {valorCompra}')
            print(f'Valor del descuento: {descuento}')
            print(f'Valor de la compra con descuento: {total}')
        elif (numColchones >= 6) and (numColchones < 8):
            valorCompra =  numColchones * valorCholchones
            descuento = (0.25 * valorCompra)
            total = valorCompra - descuento
            print(f'Se le aplicara un descuento del: 25%')
            print(f'Valor de la compra sin descuento: {valorCompra}')
            print(f'Valor del descuento: {descuento}')
            print(f'Valor de la compra con descuento: {total}')    
        else:
            valorCompra =  numColchones * valorCholchones
            descuento = (0.30 * valorCompra)
            total = valorCompra - descuento
            print(f'Se le aplicara un descuento del: 30%')
            print(f'Valor de la compra sin descuento: {valorCompra}')
            print(f'Valor del descuento: {descuento}')
            print(f'Valor de la compra con descuento: {total}')
    else:
        print(f'El valor del colchon debe ser mayor a 0')
else:
    print(f'El valor ingresado debe ser mayor a 0')
