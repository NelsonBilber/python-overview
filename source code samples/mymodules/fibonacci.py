# Modular Programming
# https://www.python-course.eu/python3_modules_and_modular_programming.php

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
