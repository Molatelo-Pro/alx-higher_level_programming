#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
     result_list = [0] * list_length
    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            result_list[i] = result
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            pass
    return result_list
