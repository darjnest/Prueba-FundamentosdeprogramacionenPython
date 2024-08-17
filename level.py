def choose_level(n_pregunta, p_level):
    
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