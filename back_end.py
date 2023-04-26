import numpy as np
from scipy import signal
from time import sleep

board = open('data/board.txt', 'r')

width, height = board.readline().split(' ')
width = int(width)
height = int(height)

matrix = np.zeros([width, height])
adjacency = np.ones([3, 3])
adjacency[1, 1] = 10
for i in range(height):
    matrix[i] = np.array(list(map(int, board.readline().split(' '))))[:width]

on = -1


def next_generation():
    global matrix, adjacency
    neighbours = signal.convolve2d(matrix, adjacency, mode='same')
    # print(neighbours)
    for y in range(height):
        for x in range(width):
            if (neighbours[y, x] // 10 == 0) and (neighbours[y, x] % 10 == 3):
                matrix[y, x] = 1
            elif neighbours[y, x] // 10 == 1 and (1 < neighbours[y, x] % 10 < 4):
                matrix[y, x] = 1
            else:
                matrix[y, x] = 0
    print(matrix)


# def turnOnOf():
#     global on
#     on *= -1
#
#
# def simulation():
#     global on
#     while True:
#         sleep(1.5)
#         if on == 1:
#             next_generation()
