import pathlib

path_to_this_file = pathlib.Path(__file__)

path_to_parent = path_to_this_file.parent

path_to_another_file = path_to_parent.joinpath('my_file.txt')

if __name__ == '__main__':
    print(f'{path_to_this_file=}')

    print(f'{path_to_parent=}')

    print(f'{path_to_another_file=}')
