from functions.write_file import write_file

def test():
    test_cases = {
        'calculator': [
            ("lorem.txt", "wait, this isn't lorem ipsum"),
            ("pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
            ("/tmp/temp.txt", "this should not be allowed")
        ]
    }

    for working_dir in test_cases:
        for target_file in test_cases[working_dir]:
            print(f"Result for '{target_file[0]}':")
            print(write_file(working_dir, *target_file))

if __name__ == "__main__":
    test()