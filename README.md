# Proyecto_SemanaTec

## 📋 Changes to Pacman

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

