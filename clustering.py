
def cluster(faces, keyfobs):
    keyfob_id, keyfob_timestamp = keyfobs.pop(0)
    clusters = [{"faces": [], "keyfob": keyfob_id}]
    while len(faces) != 0:
        if len(keyfobs) != 0 and faces[0][1] >= keyfobs[0][1]:
            # Time for a new cluster.
            keyfob_id, keyfob_timestamp = keyfobs.pop(0)
            clusters.append({"faces": [faces[0][0]], "keyfob": keyfob_id})
        else:
            clusters[-1]['faces'].append(faces[0][0])
        faces.pop(0)
    return clusters
