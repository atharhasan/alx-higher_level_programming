#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0.0
    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        result = None
    finally:
        print("{}".format(result))
    return result
     