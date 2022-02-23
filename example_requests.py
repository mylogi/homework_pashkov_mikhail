from time import sleep

import requests


def main():
    url = 'https://example.com/'
    response = requests.get(url)
    print(response.text)
    print(response.status_code)

    sleep(1)

    with requests.Session() as session:
        response = session.get(url)
        print(response.text)
        print(response.status_code)


if __name__ == '__main__':
    main()
