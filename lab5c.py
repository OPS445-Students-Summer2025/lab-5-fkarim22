#!/usr/bin/env python3
# Author ID: 147424238

def add(number1, number2):
    # Add two numbers together, return the result, if error return string 'error: could not add numbers'
    try:
        return int(number1) + int(number2)
    except (ValueError, TypeError):
        return 'error: could not add numbers'

def read_file(filename):
    # Read a file, return a list of all lines, if error return string 'error: could not read file'
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except:
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10, 5))                   # 15
    print(add('10', 5))                # 15
    print(add('abc', 5))               # error
    print(read_file('seneca2.txt'))    # works if file exists
    print(read_file('file10000.txt'))  # error
