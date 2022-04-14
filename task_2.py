"""Load data

Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .

As a result, store all comments in chronological order in JSON and dump it to a file.

"""

# Solution:

import json

import requests

url = 'https://api.pushshift.io/reddit/comment/search/'

resp = requests.get(url)

# help(resp)

# print(resp.status_code)

data_string_as_json = resp.text
data_string = json.loads(data_string_as_json)

print(f'{data_string=}\n')


# print(resp.ok)

def get_author_and_comment(data: dict) -> list:
    list_of_data: list = []
    for value in data.values():
        for i in range(len(value)):
            new_dictionary_for_list: dict = {'author': value[i]['author'], 'body': value[i]['body']}
            list_of_data.append(new_dictionary_for_list)
    # print(list_of_data)
    return list_of_data


def push_json(list_1: list) -> None:
    data_for_encoding = list_1
    data_json = json.dumps(data_for_encoding, sort_keys=False, indent=4)
    with open('json_for_task_2.json', 'w') as file:
        file.write(data_json)


def load_from_json():
    with open('json_for_task_2.json', 'r') as file:
        data_as_json = file.read()
        data_as_string = json.loads(data_as_json)
    return data_as_string


def main():
    push_json(get_author_and_comment(data_string))
    print(load_from_json())


if __name__ == '__main__':
    main()
