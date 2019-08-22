# First, generate false code.
from tabulate import tabulate
from faker import generate
faces, keyfobs = generate()
print("Faces Detected")
print(tabulate(faces, headers=['Face ID', 'Timestamp']))
print("Keyfobs Detected")
print(tabulate(keyfobs, headers=['Keyfob ID', 'Timestamp']))
