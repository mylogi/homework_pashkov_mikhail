import pathlib

path_to_this_file = pathlib.Path(__file__)

path_to_parent = path_to_this_file.parent

path_to_json_file = path_to_parent.joinpath('phone_book.json')

if __name__ == '__main__':
    print(path_to_this_file)

    print(path_to_parent)

    print(path_to_json_file)
