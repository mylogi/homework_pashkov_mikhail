import json

from path_file import path_to_json_file


def first_task_after_turn():
    phonebook_dict_json_loads = path_to_json_file.read_text()

    return json.loads(phonebook_dict_json_loads)


def first_question():
    first_input = input(
        'Hello! What does number interest you?\nDont know number - please pass s\nOr pass number:').lower()
    # if first_input == 's':
    #     return first_input
    # elif first_input.isdigit() and len(first_input) == 10:
    #     return first_input
    if first_input != 's' or (first_input.isdigit() and len(first_input) == 10):
        first_question()
    else:
        return first_input


def search(search_query, readed_data):
    if search_query == 's':
        search_input = input('\nPlease choice:\nFirst name search - F'
                             '\nLast name search - L'
                             '\nCity search - C'
                             '\nState search - S'
                             '\nFull name search - FL'
                             '\nTelephone search - T'
                             '\nDo choice: ').lower()
        if search_input in ['f', 'l', 'c', 's', 'fl', 't']:
            return search_input
    else:
        for key, value in readed_data.items():
            if key == search_query:
                print(f'{key}: {value}')
                return False


def search_first_name(search_input, readed_data):
    if not search_input:
        return False
    elif search_input == 'f':
        first_name_input = input('Enter the first name: ').lower()
        for key, value in readed_data.items():
            if value['first_name'].lower() == first_name_input:
                print(f'{key}: {value}')
                main()
            else:
                return True


def last_task_after_turn(readed_data):
    phonebook_dict_json_dumps = json.dumps(readed_data, indent=2)

    path_to_json_file.write_text(phonebook_dict_json_dumps)


def main():
    readed_data = first_task_after_turn()
    # last_task_after_turn(readed_data)
    search_query = first_question()
    search_input = search(search_query, readed_data)
    search_first_name(search_input, readed_data)


if __name__ == '__main__':
    main()
