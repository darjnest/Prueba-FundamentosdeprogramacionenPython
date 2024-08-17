import preguntas as p


def verificar(alternativas, eleccion):
    # Devuelve el índice de elección dada
    eleccion_idx = ['a', 'b', 'c', 'd'].index(eleccion)

    # Verificar si la elección es correcta
    correcto = alternativas[eleccion_idx][1] == 1
    
    return correcto

if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)






