#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            # Get the elements from both lists, defaulting to 0 if out of range
            elem_1 = my_list_1[i] if i < len(my_list_1) else 0
            elem_2 = my_list_2[i] if i < len(my_list_2) else 0
            # Perform division, handling division by zero
            if isinstance(elem_1, (int, float)) and isinstance(elem_2, (int, float)):
                if elem_2 == 0:
                    raise ZeroDivisionError
                result.append(elem_1 / elem_2)
            else:
                raise TypeError
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except TypeError:
            print("wrong type")
            result.append(0)
        except IndexError:
            print("out of range")
    return result

