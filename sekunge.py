import os
import sys

from string import ascii_lowercase as abc


variables = {letter: 0 for letter in abc}

if len(sys.argv) == 1:
    # file = input("No arguments. Please specify filename: ")
    # sys.argv.append(file)
    sys.argv.append("code.txt")

file = sys.argv[1]

if not os.path.exists(file):
    print("File does not exist.")
    exit(1)

file_contents = None
try:
    with open(file, 'r') as f:
        file_contents = f.read()
except Exception as e:
    print(f"Error reading file: {e}")

if file_contents is None:
    print("File does not contain anything.")

index = 0
character = None

def set_character():
    global index, character
    character = file_contents[index]

def next_character():
    global index, character
    index += 1
    set_character()
    return character

while index < len(file_contents):
    set_character()

    if character.isspace():
        try:
            next_character()
        except IndexError:
            break
        else:
            continue

    if not character.isalpha():
        print(f"This is not a valid character: {character}")
        break
    
    if character == "s":
        # set[variable](value)
        try:
            next_character()
        except IndexError:
            print(f"Expected a variable at index {index}.")
            break
        
        if not character.isalpha():
            print(f"Expected a variable at index {index}.")
            break

        if character not in variables:
            print(f"{character} at {index} is not a variable.")
            break
        
        variable_name = character
        try:
            next_character()
        except IndexError:
            variables[variable_name] = 0
            break
        
        value = ""

        while index+1 < len(file_contents) and not character.isspace():
            value += character
            next_character()
        
        if index+1 == len(file_contents):
            value += character

        
        if value.isdigit():
            value = int(value)
        
        variables[variable_name] = value
        try:
            next_character()
        except IndexError:
            break
        else:
            continue
    
    print(f"Invalid command: {character}")
    break

print(variables)