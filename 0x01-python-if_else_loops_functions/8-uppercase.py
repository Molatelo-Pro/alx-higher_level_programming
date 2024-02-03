#!/usr/bin/python3
def uppercase(str):
  for p in str:
    if ord(p) >= ord('a') and ord(p) <= ord('z'):
     char = chr(ord(p) - 32)
       else:
        char = p
         print("{:s}".format(char), end="")
           print('')
