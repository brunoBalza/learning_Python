jugador_1 = input("Jugador numero 1, ingrese su jugada (Piedra, Papel o Tijera): ")

jugador_2 = input("Jugador numero 2, ingrese su jugada (Piedra, Papel o Tijera): ")

if jugador_1 == jugador_2:
    print("Empate")
elif (jugador_1 == "Piedra" and jugador_2 == "Tijera") or \
     (jugador_1 == "Papel" and jugador_2 == "Piedra") or \
     (jugador_1 == "Tijera" and jugador_2 == "Papel"):
    print("Jugador 1 gana")
else:
    print("Jugador 2 gana") 