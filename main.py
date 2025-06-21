from copy import deepcopy

# Matriz del laberinto
laberinto = [
    [1, 1, 1, 3, 0, 1, 1, 1, 4],
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 0, 0, 1],
    [0, 1, 0, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 3, 1, 1],
    [3, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 3, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 4],
    [1, 1, 3, 1, 0, 1, 1, 1, 1]
]

inicio = (8, 0)
fin = (0, 0)
min_puntaje = 23

# Direcciones: arriba, derecha, abajo, izquierda
movimientos = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def es_valido(x, y, visitado):
    return (0 <= x < 9 and 0 <= y < 9 and laberinto[x][y] != 0 and not visitado[x][y])

def valor_celda(x, y):
    if (x, y) == inicio or (x, y) == fin:
        return 1
    return laberinto[x][y]

def backtrack(x, y, puntaje_actual, visitado, camino):
    if (x, y) == fin:
        if puntaje_actual >= min_puntaje:
            return True
        return False

    for dx, dy in movimientos:
        nx, ny = x + dx, y + dy
        if es_valido(nx, ny, visitado):
            visitado[nx][ny] = True
            camino.append((nx, ny))
            if backtrack(nx, ny, puntaje_actual + valor_celda(nx, ny), visitado, camino):
                return True
            camino.pop()
            visitado[nx][ny] = False
    return False

def resolver_laberinto():
    visitado = [[False] * 9 for _ in range(9)]
    camino = [inicio]
    visitado[inicio[0]][inicio[1]] = True

    if backtrack(inicio[0], inicio[1], valor_celda(*inicio), visitado, camino):
        print("¡Se encontró un camino válido con al menos 23 puntos!\n")
        mostrar_camino(camino)
    else:
        print("No se encontró un camino que cumpla con la condición de puntos.")

def mostrar_camino(camino):
    solucion = [[" " for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if laberinto[i][j] == 0:
                solucion[i][j] = "█"
            else:
                solucion[i][j] = "."

    for x, y in camino:
        solucion[x][y] = "*"

    solucion[inicio[0]][inicio[1]] = "I"
    solucion[fin[0]][fin[1]] = "F"

    for fila in solucion:
        print(" ".join(fila))

# Ejecutar
if __name__ == "__main__":
    print("Laberinto original:")
    for fila in laberinto:
        print(fila)
    print("\nBuscando camino...\n")
    resolver_laberinto()
