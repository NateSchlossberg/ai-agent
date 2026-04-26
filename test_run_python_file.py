from functions.run_python_file import run_python_file

def test():
    test_cases = {
        'calculator': [
            ('main.py',),
            ('main.py', ["3 + 5"]),
            ('tests.py',),
            ("../main.py",),
            ("nonexistent.py",),
            ("lorem.txt",),
        ]
    }

    for working_dir in test_cases:
        for command in test_cases[working_dir]:
            print( \
                f"Results for running {command[0]}{' with args ' + ",".join(command[1]) if len(command) > 1 else ''}:"
                )
            print(run_python_file(working_dir, *command))

if __name__ == "__main__":
    test()