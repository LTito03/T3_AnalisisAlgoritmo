N = 9

# Laberinto base
matriz = [
    [1, 1, 1, 3, 0, 1, 1, 1, 4],
    [3, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 1, 0, 1, 3, 1, 0],
    [3, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 0],
    [1, 0, 0, 1, 0, 1, 0, 0, 4],
    [1, 1, 3, 1, 1, 1, 1, 1, 1]
]

# Direcciones: arriba, derecha, abajo, izquierda
movimientos = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def se_puede_ir(i, j, ya_fui):
    return 0 <= i < N and 0 <= j < N and matriz[i][j] != 0 and not ya_fui[i][j]

def buscar_camino(i, j, ya_fui, camino_actual, puntos):
    if (i, j) == (0, 0):
        if puntos >= 23:
            return True, camino_actual
        else:
            return False, []

    for dx, dy in movimientos:
        siguiente_i = i + dx
        siguiente_j = j + dy

        if se_puede_ir(siguiente_i, siguiente_j, ya_fui):
            ya_fui[siguiente_i][siguiente_j] = True
            camino_actual.append((siguiente_i, siguiente_j))
            puntos_nuevos = puntos + matriz[siguiente_i][siguiente_j]

            llegamos, camino_final = buscar_camino(siguiente_i, siguiente_j, ya_fui, camino_actual, puntos_nuevos)
            if llegamos:
                return True, camino_final

            # Retroceder
            camino_actual.pop()
            ya_fui[siguiente_i][siguiente_j] = False

    return False, []

def resolver_laberinto():
    ya_fui = [[False]*N for _ in range(N)]
    ya_fui[8][0] = True
    camino = [(8, 0)]
    exito, camino_encontrado = buscar_camino(8, 0, ya_fui, camino, 1)

    if exito:
        print("¡Sí se encontró camino con 23 puntos o más!")
        salida = [[" "]*N for _ in range(N)]
        for a, b in camino_encontrado:
            salida[a][b] = "*"
        salida[8][0] = "I"
        salida[0][0] = "F"
        for fila in salida:
            print(" ".join(fila))
    else:
        print(" No hay camino con 23 puntos o más.")

resolver_laberinto()
