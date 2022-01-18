import json
import uuid

from path_file import path_to_json_file


def add_entries() -> None:
    read_data_as_string = path_to_json_file.read_text()
    readed_data = json.loads(read_data_as_string)

    first_name = input("Enter contact's first name: ")
    last_name = input("Enter contact's last name: ")
    phone_number = input("Enter contact's phone number: ")
    state = input("Enter state: ")

    readed_data.update({
        str(uuid.uuid4()): {
            'First Name': first_name,
            'Last Name': last_name,
            'Phone number': phone_number,
            'State': state
        }
    })

    load_data_as_string = json.dumps(readed_data, indent=2)
    path_to_json_file.write_text(load_data_as_string)


# def first_task_after_turn():
#     phonebook_dict_json_loads = path_to_json_file.read_text()
#
#     return json.loads(phonebook_dict_json_loads)
#
# def last_task_after_turn(readed_data):
#     phonebook_dict_json_dumps = json.dumps(readed_data, indent=2)
#
#     path_to_json_file.write_text(phonebook_dict_json_dumps)


def main():
    while True:
        print('Hello! What do you want to do?\n')
        print('1 - Add new entries')
        print('2 - Search contact')
        print('3 - Update contact')
        print('4 - Delete contact\n')

        try:
            user_choice = int(input('Your input: '))
        except ValueError:
            print('Try once more! Make a choice (1-4)')
            continue

        if user_choice == 1:
            add_entries()
        elif user_choice == 2:
            print("search")
        elif user_choice == 3:
            print("update_contact")
        elif user_choice == 4:
            print("delete_contact")
        else:
            print('No such function! Make a choice (1-4)')


if __name__ == '__main__':
    main()
