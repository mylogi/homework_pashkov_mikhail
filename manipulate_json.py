import json

from path_file import path_to_parent

users_info = [
    {
        'name': 'Bruce',
        'age': 35,
        'married': False,
        'hobbies': [
            'Programming',
            'Running',
        ],
    },
    {
        'name': 'Tony',
        'age': 42,
        'married': True,
        'hobbies': [
            'Engineering',
            'Flying',
        ],
    }
]

path_to_json_with_users = path_to_parent.joinpath('users.json')

if __name__ == '__main__':
    print(f'{users_info=}')

    data_as_string = json.dumps(users_info, indent=2)
    print(f'{data_as_string=}')

    path_to_json_with_users.write_text(data_as_string)

    readed_data_as_str = path_to_json_with_users.read_text()
    print(f'{readed_data_as_str=}')
    readed_data = json.loads(readed_data_as_str)
    print(f'{readed_data=}')
