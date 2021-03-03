numEstudiantes = float(input('Digite la cantidad de estudiante: '))
if numEstudiantes > 0:
    if numEstudiantes < 20:
        personalSeleccionado= (0.50 * numEstudiantes)
        print(f'Se seleccionara el: 50% de los estudiantes')
        print(f'Cantidad total de estudiantes: {numEstudiantes}')
        print(f'Cantidad a encuestar: {personalSeleccionado}')
    elif (numEstudiantes >= 20) and (numEstudiantes <= 30):
        personalSeleccionado= (0.60 * numEstudiantes)
        print(f'Se seleccionara el: 60% de los estudiantes')
        print(f'Cantidad total de estudiantes: {numEstudiantes}')
        print(f'Cantidad a encuestar: {personalSeleccionado}')
    else:
        personalSeleccionado= (0.70 * numEstudiantes)
        print(f'Se seleccionara el: 70% de los estudiantes')
        print(f'Cantidad total de estudiantes: {numEstudiantes}')
        print(f'Cantidad a encuestar: {personalSeleccionado}')
else:
    print(f'El valor ingresado debe ser mayor a 0')
