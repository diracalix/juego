import random


def obtener_eleccion():
    """Obtiene la elección del jugador."""
    print("¡Bienvenido al juego de Piedra, Papel o Tijeras!")
    print("Elige tu opción:")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijeras")

    eleccion = int(input("Ingresa el número de tu elección: "))
    return eleccion


def obtener_eleccion_computadora():
    """Genera una elección aleatoria para la computadora."""
    return random.randint(1, 3)


def determinar_ganador(jugador, computadora):
    """Determina quién ganó el juego."""
    opciones = ["Piedra", "Papel", "Tijeras"]
    opcion_computadora = opciones[computadora - 1]

    if jugador == computadora:
        print(f"Empate. Ambos eligieron {opcion_computadora}.")
    elif (jugador == 1 and computadora == 3) or (jugador == 2 and computadora == 1) or (jugador == 3 and computadora == 2):
        print(f"¡Ganaste! La computadora eligió {opcion_computadora}.")
    else:
        print(f"Perdiste. La computadora eligió {opcion_computadora}.")


# Obtener elecciones
eleccion_jugador = obtener_eleccion()
eleccion_computadora = obtener_eleccion_computadora()

# Determinar ganador
determinar_ganador(eleccion_jugador, eleccion_computadora)
