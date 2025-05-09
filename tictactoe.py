""" Tic Tac Toe

Version final:
Modifica el tamaño y el color de los símbolos
Validar si una casilla ya se encuentra ocupada
Determinar cuando juego haya terminad e indicar quien o si se empato
"""
import turtle
from freegames import line


# Matriz para registrar las casillas ocupadas
board = [[None for _ in range(3)] for _ in range(3)]
game_over = False  # Variable para controlar el estado del juego


def grid():
    """Dibuja el tablero de juego con 4 líneas formando cuadros 3x3."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Dibuja el símbolo X con color morado pastel."""
    turtle.color('#db7ff7')  # Morado pastel
    turtle.width(6)
    line(x + 20, y + 20, x + 113, y + 113)
    line(x + 20, y + 113, x + 113, y + 20)


def drawo(x, y):
    """Dibuja el símbolo O con color cyan pastel."""
    turtle.color('#8af0f1')  # Cyan pastel
    turtle.width(6)
    turtle.up()
    turtle.goto(x + 67, y + 25)
    turtle.down()
    turtle.circle(42)


def floor(value):
    """Convierte coordenadas a índices del tablero."""
    return ((value + 200) // 133) * 133 - 200


def get_board_index(pos):
    """Convierte coordenadas a índices de matriz."""
    return int((pos + 200) // 133)


def check_winner():
    """Revisa si hay un ganador o empate.

    Returns:
        int/None: 0 si gana X, 1 si gana O, None si no hay ganador
        bool: True si hay empate
    """
    # Verificar filas
    for row in range(3):
        if (board[row][0] == board[row][1] == board[row][2] and
                board[row][0] is not None):
            return board[row][0], False

    # Verificar columnas
    for col in range(3):
        if (board[0][col] == board[1][col] == board[2][col] and
                board[0][col] is not None):
            return board[0][col], False

    # Verificar diagonales
    if (board[0][0] == board[1][1] == board[2][2] and
            board[0][0] is not None):
        return board[0][0], False
    if (board[0][2] == board[1][1] == board[2][0] and
            board[0][2] is not None):
        return board[0][2], False

    # Verificar empate
    if all(board[row][col] is not None
           for row in range(3) for col in range(3)):
        return None, True

    return None, False


def show_message(message):
    """Muestra un mensaje en pantalla cuando termina el juego."""
    turtle.up()
    turtle.goto(0, -100)
    turtle.color('red')
    turtle.write(message, align='center', font=('Arial', 20, 'normal'))


state = {'player': 0}  # 0 para X, 1 para O
players = [drawx, drawo]  # Funciones de dibujo por turno


def tap(x, y):
    """Maneja el clic del mouse para dibujar X o O."""
    global game_over

    if game_over:
        return  # Si el juego terminó, no hacer nada

    x_pos = floor(x)
    y_pos = floor(y)

    # Convertir a índices de matriz
    col = get_board_index(x)
    row = 2 - get_board_index(y)  # Invertir filas para matriz

    # Validar si la casilla está ocupada
    if board[row][col] is not None:
        print("¡Casilla ocupada! Elige otra.")
        return

    # Marcar casilla como ocupada
    board[row][col] = state['player']

    # Dibujar símbolo
    player = state['player']
    draw = players[player]
    draw(x_pos, y_pos)
    turtle.update()

    # Verificar si hay ganador o empate
    winner, is_tie = check_winner()
    if winner is not None or is_tie:
        game_over = True
        if is_tie:
            show_message("¡Empate!")
        else:
            winner_name = "X" if winner == 0 else "O"
            show_message(f"¡Ganaron las {winner_name}!")
        return

    # Cambiar turno
    state['player'] = not player


# Configuración inicial del juego
turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
grid()
turtle.update()
turtle.onscreenclick(tap)
turtle.done()
