"""
Pacman: Classic arcade game.

Exercises:
1. Change the board.
2. Change the number of ghosts.
3. Change where Pacman starts.
4. Make the ghosts faster/slower.
5. Make the ghosts smarter.
"""

from random import choice
import turtle as t
from freegames import floor, vector

# Game state and drawing turtles
state = {'score': 0}
path = t.Turtle(visible=False)
writer = t.Turtle(visible=False)
path.hideturtle()
writer.hideturtle()

# Movement vectors for Pacman and ghosts
aim = vector(5, 0)
pacman = vector(-40, -80)
ghosts = [
    [vector(-180, 160), vector(10, 0)],
    [vector(-180, -160), vector(0, 10)],
    [vector(100, 160), vector(0, -10)],
    [vector(100, -160), vector(-10, 0)],
]

# fmt: off
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]
# fmt: on


def square(x, y):
    """
    Draw a filled wall square at the given coordinates.

    Args:
        x (int): X-coordinate of the tile's lower-left corner.
        y (int): Y-coordinate of the tile's lower-left corner.
    """
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for _ in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()


def offset(point):
    """
    Compute the index in the tiles list for a point.

    Args:
        point (vector): Position vector.

    Returns:
        int: Index in the tiles list.
    """
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    return int(x + y * 20)


def valid(point):
    """
    Check if a point is movable (not a wall).

    Args:
        point (vector): Target position.

    Returns:
        bool: True if the tile is not a wall and aligned.
    """
    idx = offset(point)
    if tiles[idx] == 0:
        return False

    idx = offset(point + 19)
    if tiles[idx] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0


def pellet_triangle(x, y, size=8):
    """
    Draw a triangular pellet centered in the tile.

    Args:
        x (int): X-coordinate of the tile's lower-left corner.
        y (int): Y-coordinate of the tile's lower-left corner.
        size (int, optional): Side length. Defaults to 8.
    """
    half = size / 2
    height = (size * (3 ** 0.5)) / 2

    path.up()
    path.goto(x + 10 - half, y + 10 - height / 3)
    path.down()
    path.begin_fill()

    for _ in range(3):
        path.forward(size)
        path.left(120)

    path.end_fill()


def world():
    """
    Draw the game board: walls and pellets.
    """
    t.bgcolor('black')
    path.color('white')

    for idx, tile in enumerate(tiles):
        if tile > 0:
            x = (idx % 20) * 20 - 200
            y = 180 - (idx // 20) * 20
            square(x, y)
            if tile == 1:
                path.color('green')
                pellet_triangle(x, y)
                path.color('white')


def move():
    """
    Update positions of Pacman and ghosts, redraw, and handle collisions.
    """
    writer.undo()
    writer.write(state['score'])

    t.clear()
    if valid(pacman + aim):
        pacman.move(aim)

    idx = offset(pacman)
    if tiles[idx] == 1:
        tiles[idx] = 2
        state['score'] += 1
        x = (idx % 20) * 20 - 200
        y = 180 - (idx // 20) * 20
        square(x, y)

    t.up()
    t.goto(pacman.x + 10, pacman.y + 10)
    t.dot(20, 'yellow')

    for point, course in ghosts:
        if valid(point + course):
            point.move(course)
        else:
            plan = choice([
                vector(10, 0), vector(-10, 0),
                vector(0, 10), vector(0, -10),
            ])
            course.x, course.y = plan.x, plan.y

        t.up()
        t.goto(point.x + 10, point.y + 10)
        t.dot(20, 'red')

    t.update()
    for point, _ in ghosts:
        if abs(pacman - point) < 20:
            return
    t.ontimer(move, 100)


def change(x, y):
    """
    Change Pacman's direction if the move is valid.

    Args:
        x (int): X component of new direction.
        y (int): Y component of new direction.
    """
    if valid(pacman + vector(x, y)):
        aim.x, aim.y = x, y


# Game setup and start
t.setup(420, 420, 370, 0)
t.hideturtle()
t.tracer(False)

writer.color('white')
writer.up()
writer.goto(160, 160)
writer.write(state['score'])

t.listen()
t.onkey(lambda: change(5, 0), 'Right')
t.onkey(lambda: change(-5, 0), 'Left')
t.onkey(lambda: change(0, 5), 'Up')
t.onkey(lambda: change(0, -5), 'Down')

world()
move()
t.done()
