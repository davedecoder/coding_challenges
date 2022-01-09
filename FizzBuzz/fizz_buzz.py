""" Print integers 1 to N, but print “Fizz” if an integer is divisible by 3, “Buzz” if an integer is divisible by 5,
and “FizzBuzz” if an integer is divisible by both 3 and 5.
"""
from typing import List


def other_fizz_buzz(size: int) -> List[str]:
    res = []
    for fizzbuzz in range(size):
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            res.append("fizzbuzz")
            continue
        elif fizzbuzz % 3 == 0:
            res.append("fizz")
            continue
        elif fizzbuzz % 5 == 0:
            res.append("buzz")
            continue
        res.append((str(fizzbuzz)))
    return res


def fizz_buzz(size: int) -> List[str]:
    res = []
    for i in range(size):
        fizzbuzz = str(i)
        if i % 3 == 0:
            fizzbuzz = "fizz"
        if i % 5 == 0:
            fizzbuzz = "buzz"
        if i % (5 * 3) == 0:
            fizzbuzz = "fizzbuzz"
        res.append(fizzbuzz)
    return res


if __name__ == "__main__":
    res_a = fizz_buzz(100)
    res_b = other_fizz_buzz(100)
    assert res_a == res_b
    print("Done")
