import random


def random_id():
    return random.randint(0, 10000)

# Returns the following datasets:
# faces, a list of [face_id, timestamp]
# keyfobs, a list of [keyfob_id, timestamp]


def generate():
    face_ids = []
    keyfob_ids = []
    for i in range(10):
        face_ids.append(random_id())
        keyfob_ids.append(random_id())

    faces = []
    keyfobs = []
    current_timestamp = 0
    for i in range(random.randint(10, 20)):
        current_timestamp += random.randint(1, 100)
        keyfobs.append([keyfob_ids[random.randint(0, 9)], current_timestamp])
        faces_count = random.randint(1, 5)
        faces_list = []
        for x in range(faces_count):
            faces_list.append(face_ids[random.randint(0, 9)])
        faces_list = list(set(faces_list))
        for face in faces_list:
            current_timestamp += random.randint(0, 2)
            faces.append([face, current_timestamp])
    return faces, keyfobs
