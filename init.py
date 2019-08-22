# First, generate fake data.
from clustering import cluster
from tabulate import tabulate
from faker import generate
faces, keyfobs = generate()
print("FACES")
print(tabulate(faces, headers=['Face ID', 'Timestamp']))
print("KEYFOBS")
print(tabulate(keyfobs, headers=['Keyfob ID', 'Timestamp']))
# Second, cluster this data into groups.
groups = []  # [{faces: [face_id, ...], keyfob: keyfob_id}, ...]
print("GROUPS")
groups = cluster(faces, keyfobs)
new_groups = []
for group in groups:
    new_groups.append(
        [", ".join([str(x) for x in group['faces']]), group['keyfob']])

print(tabulate(new_groups, headers=['Faces In Group', 'Keyfob ID']))
# Second, use scoring.
# Scoring is like this:
# [[face_id, keyfob_id, score], ...]
scores = []
