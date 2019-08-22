import random


def random_id():
    return random.randint(0, 10000)

# Returns the following datasets:
# faces, a list of [face_id, timestamp]
# keyfobs, a list of [keyfob_id, timestamp]


def generate():
    face_ids = []
    keyfob_ids = []
    identities = []
    for i in range(10):
        face_id = random_id()
        keyfob_id = random_id()
        face_ids.append(face_id)
        keyfob_ids.append(keyfob_id)
        identities.append([face_id, keyfob_id])

    faces = []
    keyfobs = []
    current_timestamp = 0
    for i in range(random.randint(10, 2000)):
        current_timestamp += random.randint(1, 100)
        # Pick a random identity
        identity = identities[random.randint(0, 9)]
        keyfobs.append([identity[1], current_timestamp])
        faces_count = random.randint(1, 5)
        faces_list = [identity[0]]
        for x in range(faces_count):
            faces_list.append(face_ids[random.randint(0, 9)])
        faces_list = list(set(faces_list))
        for face in faces_list:
            current_timestamp += random.randint(0, 2)
            faces.append([face, current_timestamp])
    return faces, keyfobs, identities
