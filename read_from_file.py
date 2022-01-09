from path_file import path_to_another_file

if __name__ == '__main__':
    data_from_file = path_to_another_file.read_text()
    print(f'{data_from_file=}')
