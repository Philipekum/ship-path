from map_generation import text_file_map, array_map
from path_finder import path_finder

def main():

    # Generates a new file map if needed
    # text_file_map()

    # np.array of values
    map = array_map()

    # Generates a path of coordinates (list of tuples)
    start, end = (0, 0), (359, 179)
    path = path_finder(map, start, end)
    print(path)

main()
