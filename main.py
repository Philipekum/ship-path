import eel
import os
import timeout_decorator
from astar_python.astar import Astar


# Finds path from start to end in an array-map
# [0: inf+] is the weight of the cell, 'None' is impassable
@timeout_decorator.timeout(1.5, timeout_exception=StopIteration)
@eel.expose
def path_finder(start: list, end: list) -> list:

    # Input check
    if not isinstance(start, list) or not isinstance(end, list):
        raise ValueError
    if len(start) != 2 or len(end) != 2:
        raise ValueError
    if not all(isinstance(x, int) for x in start) or not all(isinstance(x, int) for x in end):
        raise ValueError

    arr = array_map()

    # Change '1' to 'None' due to needs of path_finder
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                arr[i][j] = None

    astar = Astar(arr)

    return astar.run(start, end)


# Makes a filepath for map.txt
def filename_maker() -> str:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(dir_path, 'data/map.txt')


# Transforms txt-map to an array
@eel.expose
def array_map(filename: str = filename_maker()) -> list:

    with open(filename, 'r') as f:
        map = []

        for line in f.readlines():
            new_line = []

            for chars in line:
                if chars != '\n':
                    chars = int(chars)
                    new_line.append(chars)

            map.append(new_line)

    return map


def main():
    eel.init("template")
    eel.start("index.html")


if __name__ == '__main__':
    main()
