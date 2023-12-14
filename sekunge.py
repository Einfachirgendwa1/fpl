import os
import sys

from string import ascii_lowercase as abc


variables = {letter: None for letter in abc}

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
        exit(1)
    
    if character == "s":
        # set[variable](value)
        next_character()
        if character not in variables:
            print(f"{character} at {index} is not a variable.")
            exit(1)
        
        variable_name = character
        try:
            next_character()
        except IndexError:
            variables[variable_name] = None
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
    
    if character == "a":
        # add[variable](value)
        variable_name = None
        try:
            next_character()
        except IndexError:
            print(f"ADD at {index} missing a variable.")
        else:
            if character in variables:
                variable_name = variables[character]
            else:
                print(f"No variable {variable_name} found (Index: {index})")
        
        if variable_name is None:
            exit(1)

        value = ""

        while index+1 < len(file_contents) and not character.isspace():
            value += character
            next_character()
        
        if index+1 == len(file_contents):
            value += character


        if value.isdigit():
            value = int(value)

        variables[variable_name] = value
    
    index += 1

print(variables)