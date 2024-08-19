import random
import preguntas as p  
from shuffle import shuffle_alt

# Define las opciones globales 
opciones = {'basicas': [1, 2, 3],
            'intermedias': [1, 2, 3],
            'avanzadas': [1, 2, 3]}

def choose_q(dificultad):
    # Escoger preguntas por dificultad
    preguntas = list(p.pool_preguntas[dificultad].keys())
    
    # Usa las opciones globales 
    global opciones
    
    # Escoger una pregunta
    n_elegido = random.choice(opciones[dificultad])
    
    # Eliminarla del ambiente global para no escogerla de nuevo
    opciones[dificultad].remove(n_elegido)
    
    # Escoger enunciado y alternativas mezcladas
    pregunta = p.pool_preguntas[dificultad][f'pregunta_{n_elegido}']
    alternativas = shuffle_alt(pregunta)
    
    return pregunta['enunciado'], alternativas

if __name__ == '__main__':
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
