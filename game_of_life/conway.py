#pylint: disable=import-error
from custom_random import random_from_f
#pylint: enable=import-error

#CONSTANTES
ON = 1
OFF = 0
vals = [ON, OFF]

#Devuelve una matriz con valores aleatorios
def random_grid(N : int):
    """Devuelve una matriz con ON/OFF aleatorios"""
    grid = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(
                random_from_f(vals, [0.7, 0.3])
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
    return neighbors

def update(grid: list, N: int):
    """Pasa al siguiente tiempo de una matriz"""
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):

            #Calculando a los vecinos
            neighbors = count_neighbors(i, j, grid, N)

            if grid[i][j] == ON:
                if (neighbors < 2) or (neighbors > 3):
                    newGrid[i][j] = OFF
            else:
                if neighbors == 3:
                    newGrid[i][j] = ON
    return newGrid

# testGrid = random_grid(5)
# print(testGrid)
# print(f"grid[1,1] vecinos = {count_neighbors(0,0,testGrid, 5)}")
# print(update(testGrid, 5))

#Seccion dedicada a pygame