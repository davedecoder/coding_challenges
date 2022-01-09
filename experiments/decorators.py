

import functools

def write_file_row_by_row(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        iterator = func(*args, **kwargs)
        row = next(iterator, None)
        while row:
            print(row)
            row = next(iterator, None)
    return wrapper


@write_file_row_by_row
def fix_data_matrix(data_a, data_b):
    for i in data_a:
        for j in data_b:
            yield i, j


def print_data():
    a = range(1,5)
    b = range(6,10)
    fix_data_matrix(a, b)

if __name__ == "__main__":
    print_data()

