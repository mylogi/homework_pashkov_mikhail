import pathlib

path_to_this_file = pathlib.Path(__file__)

path_to_parent = path_to_this_file.parent

path_to_created_file = path_to_parent.joinpath('my_file_task1.txt')

if __name__ == '__main__':
    print(path_to_this_file)

    print(path_to_parent)

    print(path_to_created_file)
