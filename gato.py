import itertools
def ganador(juegoActual):

    def todoIgual(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    for row in juego:
        print(row)
        if todoIgual(row):
            print(f"Jugador {row[0]} Es el ganador horizontalmente!")
            return True

    for col in range(len(juego[0])):
        check = []
        for row in juego:
            check.append(row[col])
        if todoIgual(check):
            print(f"Jugador {check[0]} es el ganador verticalmente!")
            return True

    diags = []
    for idx, reverse_idx in enumerate(reversed(range(len(juego)))):
        diags.append(juego[idx][reverse_idx])

    if todoIgual(diags):
        print(f"Jugador {diags[0]} Gano diagonalmente (/)")
        return True

   
    diags = []
    for ix in range(len(juego)):
        diags.append(juego[ix][ix])

    if todoIgual(diags):
        print(f"Jugador {diags[0]} Gano diagonalmente (\\)")
        return True

    return False


def game_board(game_map, player=0, row=0, column=0, just_display=False):

    try:
        if game_map[row][column] != 0:
            print("Espacio ocupado!")
            return False
        print("Verical: columnas \n Horizontal: filas")
        print("   0  1  2")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    except IndexError:
        print("Porfavor inserte una columna valida (IndexError)")
        return False
    except Exception as e:
        print(str(e))
        return False


play = True
players = [1, 2]
while play:
    juego = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    game_won = False
    cicloJugador = itertools.cycle([1, 2])
    game_board(juego, just_display=True)
    while not game_won:
        current_player = next(cicloJugador)
        played = False
        while not played:
            print(f"Jugador: {current_player}")
            columnaElejida = int(input("Elija columna "))
            filaElejida = int(input("Elija fila "))
            played = game_board(juego, player=current_player, row=filaElejida, column=columnaElejida)

        if ganador(juego):
            game_won = True
            again = input("El juego termino, Te gustaria jugar denuevo? (y/n) ")
            if again.lower() == "y":
                print("Reiniciando!")
            elif again.lower() == "n":
                print("Adioss")
                play = False
            else:
                print("Respuesta no valida, abandonando juego.")
                play = False
