# First, generate fake data.
from clustering import cluster
from tabulate import tabulate
from faker import generate
from scoring import score
from guess import guess
faces, keyfobs, identities = generate()
faces2 = faces.copy()
keyfobs2 = keyfobs.copy()
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
scores = score(groups)
print("SCORES")
print(tabulate(scores, headers=[
      'Face ID', 'Keyfob ID', "Relationship Score"]))
faces2 = list(set([x[0] for x in faces2]))
keyfobs2 = list(set([x[0] for x in keyfobs2]))
guesses = guess(faces2, keyfobs2, scores)
newguesses = []
for guess in guesses:
    found = "-"
    nextOne = ["-", "-"]
    i = 0
    while nextOne[0] != guess[0] and i < len(identities):
        # Find the matching identity and guess.
        nextOne = identities[i]
        i += 1
    guess.append(nextOne[1])
    newguesses.append(guess)
print("IDENTITIES")
print(tabulate(newguesses, headers=[
      'Face ID', 'Keyfob ID', 'Guessed Keyfob ID']))
