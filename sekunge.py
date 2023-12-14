import os
import sys

if len(sys.argv) == 1:
    file = input("No arguments. Please specify filename: ")
    sys.argv.append(file)

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

