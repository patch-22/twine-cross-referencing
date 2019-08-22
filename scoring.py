
def add_points(face, keyfob, score, scores):
    for index in range(len(scores)):
        if scores[index][0] == face and scores[index][1] == keyfob:
            scores[index][2] += score
            return scores
    scores.append([face, keyfob, score])
    return scores


def score(clusters):
    scores = []
    for cluster in clusters:
        individual_score = 1 / len(cluster['faces'])
        for face in cluster['faces']:
            scores = add_points(
                face, cluster['keyfob'], individual_score, scores)
    return scores
