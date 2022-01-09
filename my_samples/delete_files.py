from manipulate_json import path_to_json_with_users
from path_file import path_to_another_file

if __name__ == '__main__':
    path_to_json_with_users.unlink(missing_ok=True)
    path_to_another_file.unlink()
