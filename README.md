# Prueba-FundamentosdeprogramacionenPython

# Trivia Python

Este repositorio contiene el código fuente para una trivia interactiva en Python, desarrollada como parte del desafío de fundamentos de programación.

### Estructura de Archivos

* **main.py:** Archivo principal que ejecuta la trivia.
* **preguntas.py:** Contiene los diccionarios con las preguntas y alternativas.
* **validador.py:** Contiene la función para validar las opciones ingresadas por el usuario.
* **level.py:** Contiene la función para elegir el nivel de dificultad de la pregunta.
* **shuffle.py:** Contiene la función para mezclar las alternativas de una pregunta.
* **question.py:** Contiene la función para elegir una pregunta al azar y sus alternativas.
* **print_preguntas.py:** Contiene la función para imprimir una pregunta y sus alternativas formateadas.
* **verify.py:** Contiene la función para verificar si la respuesta del usuario es correcta.

### Diagrama de Clases (si aplica)
[Incluir un diagrama de clases si la estructura del código lo amerita]

### Guía de Uso

1. **Clonar el repositorio:**
   ```bash
   git clone [se quitó una URL no válida]

### Instalar dependencias: (Si se utilizan librerías externas, indicar aquí cómo instalarlas)
Ejecutar el programa:
### python main.py

Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue estas pautas:

Fork este repositorio.
Crea una nueva rama para tu función.
Realiza tus cambios y haz commit.
Envía un Pull Request describiendo tus cambios.

## Estructura de los Archivos de Código

**Ejemplo: preguntas.py**

```python
preguntas_basicas = {
    1: {
        "enunciado": "¿Cuál es la capital de Francia?",
        "alternativas": [
            ["París", 1],
            ["Londres", 0],
            ["Roma", 0],
            ["Madrid", 0]
        ]
    },
    # ... más preguntas
}

# ... diccionarios para preguntas intermedias y avanzadas

### main.py
from validador import validate
from level import choose_level
# ... importaciones de otros módulos

def main():
    # Lógica principal del juego
    # ...

if __name__ == "__main__":
    main()