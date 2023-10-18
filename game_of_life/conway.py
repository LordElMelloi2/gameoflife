#pylint: disable=import-error
from custom_random import random_from_f
#pylint: enable=import-error
import pygame, sys

#CONSTANTES
ON = 1
OFF = 0
vals = [ON, OFF]

GRID_NODE_WITH = 15
GRID_NODE_HEIGHT = 15

CELL_COLOR = (224, 179, 72)

#Devuelve una matriz con valores aleatorios
def random_grid(N : int):
    """Devuelve una matriz con ON/OFF aleatorios"""
    grid = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(
                random_from_f(vals, [0.4, 0.6])
            )
        grid.append(row)
    return grid

def count_neighbors(i: int, j: int, grid: list, N: int):
    """Cuenta los vecinos de una casilla"""
    # newGrid = grid.copy()
    neighbors = int((grid[i][(j - 1) % N] + grid[i][(j + 1) % N] +
                grid[(i - 1) % N][j] + grid[(i + 1) % N][j] +
                grid[(i - 1) % N][(j - 1) % N] + grid[(i - 1) % N][(j + 1) % N] +
                grid[(i + 1) % N][(j - 1) % N] + grid[(i + 1) % N][(j + 1) % N]) / ON)

    # if neighbors != 0:
    #     print(f"{[grid[i][(j - 1) % N], grid[i][(j + 1) % N], grid[(i - 1) % N][j]]}")
    #     print(f"{[grid[(i + 1) % N][j], 22, grid[(i - 1) % N][(j - 1) % N]]}")
    #     print(f"{[grid[(i - 1) % N][(j + 1) % N], grid[(i + 1) % N][(j - 1) % N], grid[(i + 1) % N][(j + 1) % N]]}")
    #     print("---")

    # if neighbors != 0:
    #     print(f"{[[i, (j - 1) % N], [i, (j + 1) % N], [(i - 1) % N, j]]}")
    #     print(f"{[[(i + 1) % N, j], 22, [(i - 1) % N, (j - 1) % N]]}")
    #     print(f"{[[(i - 1) % N, (j + 1) % N], [(i + 1) % N, (j - 1) % N], [(i + 1) % N, (j + 1) % N]]}")

    return neighbors

def update(grid: list, N: int):
    """Pasa al siguiente tiempo de una matriz"""
    #Copiando matriz
    c_size = len(grid[0])
    f_size = len(grid)
    newGrid = [[grid[i][j] for j in range(c_size)] for i in range(f_size)]
    for i in range(N):
        for j in range(N):

            #Calculando a los vecinos
            neighbors = count_neighbors(i, j, grid, N)
            # if neighbors != 0:
            #     print(f"Nieghtbors[{i},{j}]: {neighbors}")

            if grid[i][j] == ON:
                if (neighbors < 2) or (neighbors > 3):
                    newGrid[i][j] = OFF
            else:
                if neighbors == 3:
                    newGrid[i][j] = ON
    return newGrid

def update_screen(lastDelta, cooldown):
    now = pygame.time.get_ticks()
    if now - lastDelta >= cooldown:
        return True
    return False

def print_matrix(grid: list, N: int):
    for i in range(N):
        print(grid[i])
    print("End Matrix")

# testGrid = random_grid(5)
# print(testGrid)
# print(f"grid[1,1] vecinos = {count_neighbors(0,0,testGrid, 5)}")
# print(update(testGrid, 5))

#Seccion dedicada a pygame

def draw_square(screen, x, y, color):
    pygame.draw.rect(screen, color, [x, y, GRID_NODE_WITH, GRID_NODE_HEIGHT])

def draw_matrix(screen, grid: list, N: int):
    for i in range(N):
        for j in range(N):
            if grid[i][j] == ON:
                draw_square(screen, i*GRID_NODE_WITH, j*GRID_NODE_HEIGHT, CELL_COLOR)
#Creacion de la ventana para pygame
pygame.init()

#Creando matriz aleatoria para pygame
N = 40
matrix = random_grid(N)
# matrix = [
#     [0,0,1,0,0,0,0,0,0,0],
#     [1,0,1,0,0,0,0,0,0,0],
#     [0,1,1,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0]
# ]
# print_matrix(matrix, N)
# matrix = update(matrix, N)
# print_matrix(matrix, N)

# print("matrix[0,1] = ", matrix[0][1])

size = (1000, 700)

#Creando ventana
screen = pygame.display.set_mode(size)
pygame.display.get_surface().fill((200,200,200))

# draw_square(screen, 0, 0, (255,0,0))
# draw_square(screen, 30, 0, (255,0,0))
draw_matrix(screen, matrix, N)

pygame.display.update()

#Inicializando reloj
lastDelta = pygame.time.get_ticks()
COOLDOWN = 100

while True:
    #Pasando tiempo antes de actualizar
    if update_screen(lastDelta, COOLDOWN):
        #Actualizamos pantalla y lastDelta
        matrix = update(matrix, N)
        pygame.display.get_surface().fill((200,200,200))
        draw_matrix(screen, matrix, N)
        pygame.display.update()
        lastDelta = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()