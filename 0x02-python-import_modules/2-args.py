#!/usr/bin/python3
import sys

def print_arguments():
    num_arguments = len(sys.argv) - 1

    print(f"Number of argument(s): {num_arguments}")

    if num_arguments > 0:
        print("Arguments:")

        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"{i}: {arg}")

    else:
        print(".")

if __name__ == "__main__":
    print_arguments()
