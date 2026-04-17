from functions.get_files_info import get_files_info

def test():
    test_cases = {
        'calculator': [
            '.',
            'pkg',
            '/bin',
            '../',
        ]
    }

    for working_dir in test_cases:
        for target_dir in test_cases[working_dir]:
            print(f"Result for '{target_dir}' directory:".replace("'.'", 'current'))
            print(get_files_info(working_dir, target_dir))

if __name__ == "__main__":
    test()