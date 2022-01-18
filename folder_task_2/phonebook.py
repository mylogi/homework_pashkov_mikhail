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


def search() -> None:
    read_data_as_string = path_to_json_file.read_text()
    readed_data = json.loads(read_data_as_string)

    search_process_result = search_function(readed_data)
    print()  # space

    for id_contact, data_contact in readed_data.items():
        if len(search_process_result) >= 2:
            print(f'{data_contact}\n---')
        elif id_contact in search_process_result:
            for k, v in data_contact.items():
                print(f'{k}: {v}')
        elif not search_process_result:
            print('There is no such contact. Try something else.')


def main():
    while True:
        print('\nHello! What do you want to do?\n')
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
            search()
        elif user_choice == 3:
            print("update_contact")
        elif user_choice == 4:
            print("delete_contact")
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
