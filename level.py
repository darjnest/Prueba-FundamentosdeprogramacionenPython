def choose_level(n_pregunta, p_level):
    """
    Determina el nivel de dificultad de una pregunta en función de su número y el nivel general del cuestionario.

    Args:
        n_pregunta (int): Número de la pregunta.
        p_level (int): Nivel general del cuestionario (2 o 3).

    Returns:
        str: Nivel de dificultad de la pregunta ('basicas', 'intermedias' o 'avanzadas').

    Esta función asigna un nivel de dificultad a una pregunta en función de los siguientes criterios:

    * **p_level = 2:**
        * Preguntas 1 y 2: Nivel básico.
        * Preguntas 3 y 4: Nivel intermedio.
        * Resto de preguntas: Nivel avanzado.
    * **p_level = 3:**
        * Preguntas 1, 2 y 3: Nivel básico.
        * Preguntas 4, 5 y 6: Nivel intermedio.
        * Resto de preguntas: Nivel avanzado.
    """
    if p_level == 2:
        if n_pregunta in [1,2]:
            level = 'basicas'
        elif n_pregunta in [3,4]:
            level = 'intermedias'
        else: 
            level = 'avanzadas'
    elif p_level == 3: 
        if n_pregunta in [1,2,3]:
            level = 'basicas'
        elif n_pregunta in [4,5,6]:
            level == 'intermedias'
        else: 
            level = 'avanzadas'
    
    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias