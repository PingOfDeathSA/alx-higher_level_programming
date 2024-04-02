#!/usr/bin/python3
def safe_print_integer(value):
    """
    Prints an integer with "{:d}".format().

    Args:
        value: The value to print.

    Returns:
        bool: True if value has been correctly printed (it means the value is an integer),
              False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    value = 89
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = -89
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = "School"
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

