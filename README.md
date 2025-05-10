# Proyecto_SemanaTec

## 📋 Cambios a Pacman

### 🎮 Nuevo diseño de “comida”
- Se reemplazó el punto (`dot`) por **triángulos equiláteros** para representar las píldoras.
- Función `pellet_triangle(x, y, size)` centrada en cada casilla, con tamaño configurable.

### 👻 Fantasmas más veloces
- Incremento de la velocidad de los fantasmas: los vectores de movimiento pasan de ±5 a **±10** unidades.
- Al chocar contra un muro, el fantasma elige al azar una nueva dirección igual de rápida.

### 🛠 Reestructuración y docstrings PEP 8
- Separación clara de importaciones (estándar, terceros).
- Docstrings detallados en todas las funciones:
  - Descripción.
  - Parámetros (`Args`).
  - Valor de retorno (`Returns`), cuando aplica.
- Líneas limitadas a ≤ 79 caracteres y uso de nombres descriptivos.
- Agrupación lógica de bloques (configuración, utilidades, dibujo, lógica de juego, inicio).

### ⚙️ Cómo ajustar
- **Tamaño del triángulo**: modifica el parámetro `size` en `pellet_triangle()`.
- **Velocidad de fantasmas**: cambia los vectores en la lista `ghosts`.
