numTelevisores = int(input('Digite la cantidad de televisores a comprar: '))
valorTelvisor = float(input('Digite el valor de cada televisor: '))
numCedula = int(input('Digite su numero de cedula: '))

if numTelevisores > 0:
    if valorTelvisor > 0:
            if len(str(numCedula))>= 3:
                if str(numCedula)[-2:] == "01":
                    valorCompra =  numTelevisores * valorTelvisor
                    descuento = (0.10 * valorCompra)
                    total = valorCompra - descuento
                    print(f'Se le aplicara un descuento del: 10%')
                    print(f'Valor de la compra sin descuento: {valorCompra}')
                    print(f'Valor del descuento: {descuento}')
                    print(f'Valor de la compra con descuento: {total}')
                elif str(numCedula)[-2:] == "25":
                    valorCompra =  numTelevisores * valorTelvisor
                    descuento = (0.20 * valorCompra)
                    total = valorCompra - descuento
                    print(f'Se le aplicara un descuento del: 20%')
                    print(f'Valor de la compra sin descuento: {valorCompra}')
                    print(f'Valor del descuento: {descuento}')
                    print(f'Valor de la compra con descuento: {total}')
                elif str(numCedula)[-2:] == "44":
                    valorCompra =  numTelevisores * valorTelvisor
                    descuento = (0.35 * valorCompra)
                    total = valorCompra - descuento
                    print(f'Se le aplicara un descuento del: 35%')
                    print(f'Valor de la compra sin descuento: {valorCompra}')
                    print(f'Valor del descuento: {descuento}')
                    print(f'Valor de la compra con descuento: {total}')
                elif str(numCedula)[-2:] == "57":
                    valorCompra =  numTelevisores * valorTelvisor
                    descuento = (0.50 * valorCompra)
                    total = valorCompra - descuento
                    print(f'Se le aplicara un descuento del: 50%')
                    print(f'Valor de la compra sin descuento: {valorCompra}')
                    print(f'Valor del descuento: {descuento}')
                    print(f'Valor de la compra con descuento: {total}')    
                else:
                    total =  numTelevisores * valorTelvisor
                    print(f'Valor total a pagar: {total}') 
            else:
                print(f'La cedula debe tener un minimo de 3 numeros')
    else:
        print(f'El valor del televisor debe ser mayor a 0')
else:
    print(f'La cantidad de televisores a comprar debe ser mayor a 0 ')
