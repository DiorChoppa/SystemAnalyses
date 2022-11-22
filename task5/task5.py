import json
import numpy as np

def task(ranking_str_1: str, ranking_str_2:str) -> str:
    ranking1 = json.loads(ranking_str_1)
    ranking2 = json.loads(ranking_str_2)

    m1 = relationship_matrix(ranking1)
    m1_t = m1.transpose()

    m2 = relationship_matrix(ranking2)
    m2_t = m2.transpose()

    m12 = np.multiply(m1, m2)
    m12_t = np.multiply(m1_t, m2_t)

    conflicts = []

    for i in range(m12.shape[0]):
        for j in range(m12[i].shape[1]):
            if int(m12[i,j]) == 0 and int(m12_t[i,j]) == 0:
                if (str(j+1),str(i+1)) not in conflicts:
                    conflicts.append((str(i+1),str(j+1)))

    return json.dumps(conflicts)


def relationship_matrix(ranking):
    ranks = dict()
    rank_len = ranking_length(ranking)
    for i, rank in enumerate(ranking):
        if type(rank) is str:
            ranks[int(rank)] = i
        else:
            for r in rank:
                ranks[int(r)] = i

    return np.matrix([[1 if ranks[i+1] <= ranks[j+1] else 0 for j in range(rank_len)] for i in range(rank_len)])

def ranking_length(ranking) -> int:
    length = 0;
    for i in ranking:
        if type(i) is str:
            length+=1
        else:
            length+=len(i)
    return length
