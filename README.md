# Calculadora Científica en Python

Calculadora científica de consola, construida desde cero en Python, sin usar `eval()` ni `ast.parse()`. Implementa su propio lexer, el algoritmo Shunting-Yard (infijo → RPN) y un evaluador de notación polaca inversa (RPN) con pila.

## Características

**Operadores:** `+ - * / ^ %`

**Paréntesis:** `( )`

**Funciones:** `sin cos tan ln log sqrt`

**Constantes:** `pi`, `e`

**Factorial:** `!` (ej. `5!`)

**Números negativos:** soportados en cualquier posición de la expresión (ej. `-5+3`, `3*-2`, `(-5+3)`)

## Cómo usarlo

Desde la carpeta del proyecto, ejecutá:

```bash
python main.py
```

El programa va a pedirte expresiones matemáticas una por una. Escribí `salir` para terminar.

Ejemplo de uso:

```
Ingresá una expresión (o 'salir' para salir): 2+3*4
Resultado: 14.0
Ingresá una expresión (o 'salir' para salir): sin(pi)
Resultado: 0.0
Ingresá una expresión (o 'salir' para salir): salir
```

## Decisiones de arquitectura

**Estrategia de evaluación — Shunting-Yard → RPN → evaluación con pila.**
Se descartó `eval()` por el riesgo de seguridad de ejecutar texto arbitrario como código Python, y `ast.parse()` por acoplar la calculadora a la gramática interna de Python en vez de tener control total sobre la sintaxis propia del proyecto.

**Tipo numérico — `float`.**
Se eligió `float` en vez de `Decimal` porque las funciones científicas (`sin`, `log`, `sqrt`) del módulo `math` trabajan nativamente con `float`, evitando conversiones constantes.

**Ángulos — radianes.**
Las funciones trigonométricas trabajan en radianes en esta versión, por compatibilidad directa con `math.sin()`, `math.cos()` y `math.tan()`, que esperan radianes de forma nativa. Un modo en grados (DEG) queda documentado como mejora futura.

**Números negativos — resueltos en el lexer (`tokenizar`), no en el algoritmo Shunting-Yard.**
El símbolo `-` es ambiguo: puede ser un operador binario (resta, `8-5`) o un signo unario (número negativo, `-5`). Se resolvió esta ambigüedad en la etapa más temprana posible (el lexer), de modo que un número negativo llegue ya armado como un solo token (ej. `'-5'`) a las etapas siguientes. Esto evitó modificar el algoritmo Shunting-Yard, que no necesita saber que esta ambigüedad existe.

**Precedencia y asociatividad — `OPERATOR_INFO`.**
Cada operador tiene una precedencia numérica (qué tan "fuerte" es) y una asociatividad (`'izquierda'` o `'derecha'`, o `'no aplica'` para operadores unarios como `!` y las funciones). La asociatividad derecha de `^` garantiza que `2^3^2` se resuelva como `2^(3^2) = 512`, y no como `(2^3)^2 = 64`.

## Estructura del proyecto

| Archivo | Responsabilidad |
|---|---|
| `requisitos.py` | Listas de símbolos soportados y el diccionario `OPERATOR_INFO` (precedencia y asociatividad) |
| `funciones.py` | Motor core: lexer (`tokenizar` y sus funciones auxiliares), Shunting-Yard (`shunting_yard`), y evaluador RPN (`evaluar_rpn`) |
| `main.py` | Interfaz de consola: pide expresiones al usuario, llama a `calcular()`, y maneja errores de forma amigable |

## Nota de Riesgo — cómo se puede romper este código

Esta sección documenta honestamente los límites conocidos de la calculadora.

- **División y módulo entre cero** (`5/0`, `5%0`) → se detectan explícitamente y lanzan `ZeroDivisionError` con mensaje descriptivo, en vez de crashear.
- **Paréntesis sin cerrar** (`(2+3`) → provoca un error al intentar vaciar la pila de operadores buscando un `(` que no está (`IndexError` no controlado explícitamente — limitación conocida, no captado por los `except` actuales de `main.py`).
- **Números extremadamente grandes** (`10^10000`) → Python puede calcularlo, pero el resultado puede ser lento de procesar o poco práctico para mostrar en pantalla.
- **Símbolos no soportados** (`@`, `#`, etc.) → detectados por el lexer, lanzan `SyntaxError`.
- **Raíz cuadrada de un número negativo** (`sqrt(-9)`) → matemáticamente no tiene resultado real; se detecta explícitamente y lanza `ValueError`.
- **Factorial de un número negativo** (`-5!`) → no está definido; se detecta explícitamente y lanza `ValueError`.
- **Factorial de un número decimal** (`3.5!`) → no está definido para esta implementación; se detecta explícitamente y lanza `ValueError`.
- **Logaritmo de un número negativo o cero** (`log(-20)`, `ln(0)`) → no está definido; se detecta explícitamente y lanza `ValueError`.
- **Modo de ángulos fijo en radianes** → si un usuario ingresa un ángulo pensando en grados (ej. `sin(90)` esperando el resultado de 90°), va a obtener un resultado incorrecto respecto a lo que esperaba, ya que `90` se interpreta como radianes. No es un bug, pero es una limitación de diseño a tener en cuenta.
- **Espacios en la expresión** (`3 + 5`) → soportados y ignorados correctamente por el lexer.

### Limitación conocida sin resolver

El caso de un paréntesis sin cerrar (ej. `(2+3`) no está cubierto por un mensaje de error propio y explícito — actualmente termina en un error nativo de Python (`IndexError`) que no es capturado por los `except` de `main.py`. Queda documentado como mejora pendiente para una futura versión.
