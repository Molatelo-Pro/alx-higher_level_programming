#!/usr/bin/python3
def remove_char_at(str, n):

 if 0 <= n < len(str):
    return str[:n] + str[n+1:]
 elif n < 0 and abs(n) <= len(str):
    return str[:n] + str[n+1:]
 else:
    return str
