""" Tic Tac Toe 

Mejoras implementadas:
1. Cambio de colores a los simbolos 
2. Líneas más gruesas (ancho 6) para mejor visibilidad
3. Posicionamiento y dimension optimizada de los símbolos
4. Documentación del código

"""

import turtle
from freegames import line

def grid():
    """Draw tic-tac-toe grid with 4 lines forming 3x3 squares"""
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
