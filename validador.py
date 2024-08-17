def validate(opciones, eleccion):
    # Definir validación de eleccion
    while eleccion not in opciones:
        print(f'Opción no válida. Ingrese una opción válida: {opciones}')
        eleccion = input('Ingresa una opción: ').lower()
    
    return eleccion

if __name__ == '__main__':
    eleccion = input('Ingresa una Opción: ').lower()
    numeros = ['0', '1']
    validate(numeros, eleccion)

    
    
