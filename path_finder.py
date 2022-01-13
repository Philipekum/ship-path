from astar_python.astar import Astar
import numpy as np


# Finds path from start to end in an array-map
# (0: inf+) is the weight of the cell, 'None' is impassable
def path_finder(array, start, end):
    astar = Astar(array)

    return astar.run(start, end)


# Creates same resolution array of zeros and adds path to it
# def path_visualizer(path, map):
#
#     # Zero-array of size
#     res = np.zeros_like(map.T, dtype=object)
#
#     for i in path:
#         res[i[0]][i[1]] = '>'
#
#     return res
