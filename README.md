# FirstWeekChallenge – Reto II  
## Parte 1 – Ejecución de Tests de APIs (PokéAPI y SWAPI)

Este proyecto contiene **tests automatizados en Python** utilizando **pytest** para validar respuestas de dos APIs públicas:

- PokéAPI  
- Star Wars API (swapi.info)

Los tests verifican:
- Status codes (200 / 404)
- Contenido esperado en la respuesta
- Manejo de IDs inexistentes
- Formatos inválidos
- Cálculo de altura promedio de Pokémon de tipo *fire*

---

## Requisitos

- Python **3.10+** (recomendado)

---

## Ejecución

Instalar dependencias y ejecutar los tests:

pip install -r requirements.txt  
pytest
