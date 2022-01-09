import pathlib

path_to_this_file = pathlib.Path(__file__)

path_to_parent = path_to_this_file.parent

if __name__ == '__main__':
    print(path_to_this_file)

    print(path_to_parent)
