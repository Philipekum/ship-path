import eel
from astar_python.astar import Astar


# Finds path from start to end in an array-map
# [0: inf+] is the weight of the cell, 'None' is impassable
@eel.expose
def path_finder(start, end):
    arr = array_map()

    # Change '1' to 'None' due to needs of path_finder
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                arr[i][j] = None

    astar = Astar(arr)

    return astar.run(start, end)


# Transforms txt-map to an array
@eel.expose
def array_map(filename='Data/map.txt'):

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
