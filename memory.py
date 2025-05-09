from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(range(8)) * 2  # Solo 8 pares
state = {'mark': None}
hide = [True] * 16  # Solo 16 casillas
pairs_found = 0  # Contador de pares descubiertos


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index for 4x4 grid."""
    return int((x + 100) // 50 + ((y + 100) // 50) * 4)


def xy(count):
    """Convert tiles count to (x, y) coordinates for 4x4 grid."""
    return (count % 4) * 50 - 100, (count // 4) * 50 - 100


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global pairs_found
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        pairs_found += 1  # Aumenta contador al encontrar un par


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    # Mostrar número de pares descubiertos
    up()
    goto(-90, 110)
    color('black')
    write(f'Pares descubiertos: {pairs_found}', font=('Arial', 14, 'normal'))

    for count in range(16):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    # Verificar si se terminaron de descubrir todos los pares
    if all(not h for h in hide):
        up()
        goto(-60, 0)
        color('green')
        write('¡Has ganado!', font=('Arial', 20, 'bold'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(220, 240, 370, 0)  # Ajuste al tamaño del tablero 4x4
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
