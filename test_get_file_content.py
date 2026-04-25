from config import *
from functions.get_file_content import get_file_content

def test():
    test_large_file()

    test_cases = [
        ("calculator", "main.py"),
        ("calculator", "pkg/calculator.py"),
        ("calculator", "/bin/cat"),
        ("calculator", "pkg/does_not_exist.py"),
    ]

    for tc in test_cases:
        print('------------')
        print(f"Getting file content from {tc[1]} (working_dir: {tc[0]})")
        print(get_file_content(tc[0], tc[1]))
 

def test_large_file():
    large_filepath = "lorem.txt"
    print(f"Reading large text ({large_filepath})...")
    large_content = get_file_content("calculator", large_filepath)
    print(f"Length: {len(large_content)}")
    trunc_msg_ln = len(f'[...File "{large_filepath}" truncated at {READ_MAX_CHARS} characters]')
    print(f"Tail string:")
    print(large_content[-trunc_msg_ln:])



if __name__ == "__main__":
    test()     

