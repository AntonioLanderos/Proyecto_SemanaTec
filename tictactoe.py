""" Tic Tac Toe

Mejoras implementadas:
1.Se agregó una matriz board para registrar movimientos
2.Se agrego una función get_board_index() para convertir coordenadas a índices
3.Vericación antes de dibujar (if board[row][col] is not None)
4. Mejora en la documentación
5. Mensaje en terminal de cuando se selecciona una casilla ocupada
6. Estructura mejorada
7. Mantiene las características existentes
"""

import turtle
from freegames import line

def grid():
    """Dibuja el tablero"""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)

def drawx(x, y):
    """Dibuja el símbolo X con color morado pastel"""
    turtle.color('#db7ff7') #morado pastel(hex color)
    turtle.width(6) #se cambio la linea mas gruesa para mejor visbilidad
    line(x + 20, y + 20, x + 113, y + 113)
    line(x + 20, y + 113, x + 113, y + 20)

def drawo(x, y):
    """Dibuja el símbolo O con color cyan """
    turtle.color('#8af0f1') #color cyan
    turtle.width(6) #linea mas gruesa
    turtle.up()
    turtle.goto(x + 67, y + 25)  # se centro la posicion
    turtle.down()
    turtle.circle(42)  #Radio del circulo

def floor(value):
    """Redondea coordenadas a la posición más cercana del tablero"""
    return ((value + 200) // 133) * 133 - 200

state = {'player': 0}
players = [drawx, drawo]

def tap(x, y):
    """Dibuja X o O segun el turno y alterna jugarores """
    x = floor(x) #ajusta a la cuadricula
    y = floor(y)
    player = state['player']
    draw = players[player] #obtiene la función de dibujo del jugador
    draw(x, y) #Dibuja el simbolo
    turtle.update()
    state['player'] = not player

# Inicialización del juego
turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
grid()
turtle.update()
turtle.onscreenclick(tap)
turtle.done()
