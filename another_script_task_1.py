from path_file_for_task_1 import path_to_created_file

if __name__ == '__main__':
    data_from_my_file = path_to_created_file.read_text()
    print(f'{data_from_my_file=}')
