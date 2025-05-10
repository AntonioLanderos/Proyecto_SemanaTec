# Proyecto_SemanaTec


# Tic Tac Toe- Alejandra Montelongo A01612296
### Mejoras en la lógica del juego
- **Detección de ganador**:
  - Algoritmo que verifica patrones en filas, columnas y diagonales
  - Sistema de evaluación de tablero en tiempo real
- **Gestión de empates**:
  - Detección automática cuando no hay movimientos válidos
  - Visualización de mensaje de empate

### ️ Interfaz de Usuario
- **Diseño visual mejorado**:
  - Símbolos personalizados: 
    - X en morado pastel (#db7ff7)
    - O en cyan brillante (#8af0f1)
  - Grosor de líneas aumentado (6px) para mejor visibilidad
  - Mensajes gráficos de resultado (ganador/empate)
  - Posicionamiento y dimensión optimizada de los símbolos

### Validación
 - Verificación antes de dibujar
  - Bloqueo de casillas ocupadas
    - Mensaje en la terminal de cuando se selecciona una casilla ocupada
- Cumplimiento de estándares:
  - Flake8
- Documentación del código

## 📋 Changes to Pacman - Juan Antonio Landeros Velázquez A00574000

### 🎮 New “Food” Design
- The dot (`dot`) has been replaced with **equilateral triangles** to represent the pellets.
- The `pellet_triangle(x, y, size)` function is centered in each tile, with a configurable size.

### 👻 Faster Ghosts
- Ghost speed increased: movement vectors changed from ±5 to **±10** units.
- When hitting a wall, a ghost randomly chooses a new direction at the same speed.

### 🛠 Refactoring and PEP 8 Docstrings
- Clear separation of imports (standard, third-party).
- Detailed docstrings in all functions:
  - Description.
  - Parameters (`Args`).
  - Return value (`Returns`), when applicable.
- Lines limited to ≤ 79 characters and use of descriptive names.
- Logical grouping of code blocks (setup, utilities, rendering, game logic, startup).

### ⚙️ How to Adjust
- **Triangle Size**: modify the `size` parameter in `pellet_triangle()`.
- **Ghost Speed**: change the vectors in the `ghosts` list.

![image](https://github.com/user-attachments/assets/2e7b5506-c56e-4135-8f72-8845c3e02d50)

## Actividad Memory

🔢 Reduced the board size from an 8x8 grid (64 tiles) to a 4x4 grid (16 tiles), using only 8 pairs.

🎯 Updated the coordinate logic in the index() and xy() functions to work with the new 4-column layout.

🔄 Adjusted loops and lists to handle 16 tiles instead of 64 (tiles, hide, and drawing loop).

🖼️ Modified the screen size with setup() to better center the smaller board on the screen.

📊 The game still tracks pairs found and displays a win message when all pairs are matched.

![image](https://github.com/user-attachments/assets/c74be797-ea45-4608-8ed8-ea73f1360640)

