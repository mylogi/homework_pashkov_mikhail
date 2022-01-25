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


def search_function(readed_data: dict) -> list:
    # noinspection PyGlobalUndefined
    global user_search_choice

    while True:
        print('\nYou\'re in search! Following down\n')
        print('1 - Search by first name')
        print('2 - Search by last name')
        print('3 - Search by full name')
        print('4 - Search by phone number')
        print('5 - Search by state / city\n')

        try:
            user_search_choice = int(input('Your input: '))
            break
        except ValueError:
            print('Try once more! Make a choice (1-5)')
            continue

    data_from_the_user = 0
    print()  # space
    if user_search_choice == 1:
        data_from_the_user = input('Enter first name: ')
    elif user_search_choice == 2:
        data_from_the_user = input('Enter last name: ')
    elif user_search_choice == 3:
        data_from_the_user = input('Enter full name: ')
    elif user_search_choice == 4:
        data_from_the_user = input('Enter phone number: ')
    elif user_search_choice == 5:
        data_from_the_user = input('Enter state / city: ')
    # elif user_search_choice >= 6:
    #     print('\nThere is no such option! Try again.')

    list_of_id_contacts = []
    for id_contact, data_contact in readed_data.items():
        full_name_list = []
        for k, v in data_contact.items():
            if v == data_from_the_user and user_search_choice != 3:
                list_of_id_contacts.append(id_contact)
            elif user_search_choice == 3:
                if k in ['First Name', 'Last Name']:
                    full_name_list.append(v)
                    if ' '.join(full_name_list) == data_from_the_user:
                        list_of_id_contacts.append(id_contact)
    return list_of_id_contacts


def search():
    read_data_as_string = path_to_json_file.read_text()
    readed_data = json.loads(read_data_as_string)

    search_process_result = search_function(readed_data)
    print()  # space

    if not search_process_result:
        print('There is no such contact. Try something else.')
    else:
        for id_contact, data_contact in readed_data.items():
            if len(search_process_result) >= 2:
                print(f'{data_contact}\n---')
            elif id_contact in search_process_result:
                for k, v in data_contact.items():
                    print(f'{k}: {v}')


def delete_contact() -> None:
    read_data_as_string = path_to_json_file.read_text()
    readed_data = json.loads(read_data_as_string)

    print('Please, select a contact card to delete.')
    search_process_result = search_function(readed_data)

    for id_contact, data_contact in readed_data.items():
        if len(search_process_result) >= 2:
            print(f'{data_contact}\n---')
        elif id_contact in search_process_result:
            for k, v in data_contact.items():
                print(f'{k}: {v}')
        elif not search_process_result:
            print('There is no such contact. Try something else.')
    if search_process_result != [] and type(search_process_result) == list:
        user_agreement = input('\nDo you agree to delete these contacts? (y/n): ').lower()
        if user_agreement == 'y':
            for id_item in search_process_result:
                del readed_data[id_item]
            load_data_as_string = json.dumps(readed_data, indent=2)
            path_to_json_file.write_text(load_data_as_string)


def print_for_update_contact():
    print('What do you want to change in contact?\n')
    print('1 - First Name')
    print('2 - Last Name')
    print('3 - Phone Number')
    print('4 - State/City\n')


def update_contact() -> None:
    # noinspection PyGlobalUndefined
    global user_choice_for_update, selected_contact_card

    read_data_as_string = path_to_json_file.read_text()
    readed_data = json.loads(read_data_as_string)

    search_process_result = search_function(readed_data)
    print()  # space

    for id_contact, data_contact in readed_data.items():
        if id_contact in search_process_result:
            for k, v in data_contact.items():
                print(f'{k}: {v}')
            print()
    if type(search_process_result) == str:
        print(search_process_result)
    elif not search_process_result:
        print('There is no such contact. Try something else.')

    if search_process_result != [] and type(search_process_result) == list:
        if len(search_process_result) > 1:
            unique_search_process_result = []
            user_input_phone_number = input("More than one contact found. Enter the desired contact's number: ")
            for id_contact_2, data_contact_2 in readed_data.items():
                if id_contact_2 in search_process_result:
                    for k, v in data_contact_2.items():
                        if k == 'Phone number' and v == user_input_phone_number:
                            unique_search_process_result.append(id_contact_2)

            print_for_update_contact()

            while True:
                try:
                    user_choice_for_update = int(input('Your input: '))
                    break
                except ValueError:
                    print('Try once more! Make a choice (1-4)')
            try:
                selected_contact_card = readed_data.get(unique_search_process_result[0])
            except IndexError:
                print('\nSorry is not exist number')
                main()
    else:
        print_for_update_contact()
        while True:
            try:
                user_choice_for_update = int(input('Your input: '))
                break
            except ValueError:
                print('Try once more! Make a choice (1-4)')
                continue

        selected_contact_card = readed_data.get(search_process_result[0])
    if user_choice_for_update == 1:
        new_name = input('Please, enter new name: ')
        selected_contact_card['First Name'] = new_name
    elif user_choice_for_update == 2:
        new_name = input('Please, enter new last name: ')
        selected_contact_card['Last Name'] = new_name
    elif user_choice_for_update == 3:
        new_phone = input('Please, enter new phone number: ')
        selected_contact_card['Number'] = new_phone
    elif user_choice_for_update == 4:
        new_state = input('Please, enter new state: ')
        selected_contact_card['State'] = new_state
    else:
        print('No such function! Next time make a choice (1-4)')
    load_data_as_string = json.dumps(readed_data, indent=2)
    path_to_json_file.write_text(load_data_as_string)


def exit_from_the_program() -> int:
    exit_input = input('\nDo you want to continue? (y/n): ').lower()
    if exit_input == 'n':
        return 1
    elif exit_input == 'y':
        return 2
    else:
        return 3


def main():
    while True:
        print('\nHello! What do you want to do?\n')
        print('1 - Add new entries')
        print('2 - Search contact')
        print('3 - Update contact')
        print('4 - Delete contact')
        print('5 - Exit\n')

        try:
            user_choice = int(input('Your input: '))
        except ValueError:
            print('Try once more! Make a choice (1-4)')
            continue

        if user_choice == 1:
            add_entries()
        elif user_choice == 2:
            search()
        elif user_choice == 3:
            update_contact()
        elif user_choice == 4:
            delete_contact()
        elif user_choice == 5:
            x = exit_from_the_program()
            if x == 1:
                break
            elif x == 2:
                continue
            elif x == 3:
                print("\nWrong pass! Try 'y' or 'no'.")
                continue
        else:
            print('No such function! Make a choice (1-4)')


if __name__ == '__main__':
    main()

# def first_task_after_turn():
#     phonebook_dict_json_loads = path_to_json_file.read_text()
#
#     return json.loads(phonebook_dict_json_loads)
#
# def last_task_after_turn(readed_data):
#     phonebook_dict_json_dumps = json.dumps(readed_data, indent=2)
#
#     path_to_json_file.write_text(phonebook_dict_json_dumps)
