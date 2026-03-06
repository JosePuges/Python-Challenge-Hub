import random

def pedir_numero():
    try:
        valor = int(input("Introdce un numero: "))
        return valor
    except ValueError:
        print("ERROR, introduce un numero valido")

def jugar_partida():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    print(" ¡ Nueva partida ! He pensado un numero del 1 al 100. ¿ Podras adivinarlo ?")
    while True:
        intento = pedir_numero()
        intentos = +1
        if intento < numero_secreto:
            print(" El numero es mas alto")
        elif intento > numero_secreto:
            print(" El numero es mas bajo")
        else:
            print(f" Enhorabuena has acetado el numero en {intentos} intentos")
            return intentos    
        
def main():
    seguir_jugando = "s"
    mejor_puntuacion = None

    while seguir_jugando.lower() == "s":
        resultado = jugar_partida()


    if mejor_puntuacion is None or resultado < mejor_puntuacion:
        mejor_puntuacion = resultado
        print(f" ¡ Nuevo record : {mejor_puntuacion} intentos !")
    else:
        print(f" ¡ Tu mejor puntuacion sigue siendo: {mejor_puntuacion} intentos!")

        seguir_jugando = input(" ¿ Quieres seguir jugando ?: s/n")

    print(f" Fin del juego, tu mejor puntuaciona ha sido. {mejor_puntuacion} intentos")


    if __name__ == "__main__":
        main()