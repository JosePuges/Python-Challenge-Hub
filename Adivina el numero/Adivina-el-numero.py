import random

def juego():
    # 1. Generar número aleatorio (1-100)
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = True

    print("--- ¡Bienvenido al juego de adivinar el número! ---")
    print("He pensado un número entre 1 y 100. ¿Puedes adivinarlo?")

    # El bucle se repite hasta que el usuario acierte
    while adivinado:
        # 2. Pedir al usuario que intoduzca un número
        try:
            intento_usuario = int(input("Introduce tu número: "))
            intentos += 1 # Contador de intentos
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue

        # Comparar y dar pistas
        if intento_usuario < numero_secreto:
            print("Pista: El número es MAYOR ↑")
        elif intento_usuario > numero_secreto:
            print("Pista: El número es MENOR ↓")
        else:
            # 5. Mensaje ganador
            print(f"\n¡FELICIDADES!  Has acertado en {intentos} intentos.")
            adivinado = False

    # 7. Volver a empezar
    jugar_de_nuevo = input(" ¿Quieres jugar otra vez? (s/n): ").lower()
    if jugar_de_nuevo == 's':
        juego()
    else:
        print("¡Gracias por jugar! Hasta la próxima.")

# Iniciar el juego
juego()