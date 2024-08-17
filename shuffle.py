import preguntas as p
import random

def shuffle_alt(pregunta):
    # Mezclar alternativas
    alternativas = pregunta['alternativas']
    random.shuffle(alternativas)
    return alternativas

if __name__ == '__main__':
    # Si se ejecuta el programa varias veces las alternativas debieran aparecer en distinto orden
    print(shuffle_alt(p.pool_preguntas['basicas']['pregunta_1'])) 
