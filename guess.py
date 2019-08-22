
def guess(faces, keyfobs, scores):
    guesses = []  # [face_id, [keyfob_id, keyfob_id...]]
    for face in faces:
        highest_score = 0
        highest_score_keyfob = 0
        for score in scores:
            face_id, keyfob_id, relationship_score = score
            if face_id != face:
                continue
            if relationship_score >= highest_score:
                highest_score = relationship_score
                highest_score_keyfob = keyfob_id
        guesses.append([face, highest_score_keyfob])
    return guesses
