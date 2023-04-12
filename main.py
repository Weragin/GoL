import numpy as np
import scipy as sp

board = open('data/board.txt', 'r')

width, height = board.readline().split(' ')
width = int(width)
height = int(height)

matrix = np.zeros([width, height])
adjacency = np.ones([3, 3])
adjacency[1, 1] = 10
print(adjacency)
for i in range(height):
    matrix[i] = np.array(list(map(int, board.readline().split(' '))))[:width]


def next_generation():
    global matrix, adjacency
    neighbours = sp.signal.convolve2d(matrix, adjacency, mode='same')
    #print(neighbours)
    for i in range(height):
        for j in range(width):
            print(neighbours[i, j])
            if (neighbours[i, j]//10 == 0) and (neighbours[i, j]%10 == 3):
                #print('Born', i, j, 'Neighbours:', neighbours[i, j])
                matrix[i, j] = 1
            if neighbours[i, j]//10 == 1 and (1 < neighbours[i, j]%10 < 4):
                matrix[i, j] = 1
    print(matrix)



next_generation()
