def read_input() -> [str]:
    with open('input.txt', 'r') as f:
        return f.read().splitlines()


def read_test_input() -> [str]:
    with open('test_input.txt', 'r') as f:
        return f.read().splitlines()


def read_test_answer() -> str:
    with open('test_answer.txt', 'r') as f:
        return f.read()


def read_input_no_split() -> [str]:
    with open('input.txt', 'r') as f:
        return f.read()


def read_input_as_int() -> [int]:
    with open('input.txt', 'r') as f:
        inputs = f.read().splitlines()
        return list(map(lambda i: int(i), inputs))
