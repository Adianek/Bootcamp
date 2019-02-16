def add_matrices(m1, m2):
    # e.q. m1 = [[1,2],[2.3]]
    m3 = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m1[i])):
            row.append(m1[i][j] + m2[i][j])
        m3.append(row)
    return m3


def sub_matrices():
    pass


def _add_or_matrices(m1, m2, sign=1):
    """If add, then sign=1, if sub then sign=-1"""
    m3 = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m1[i])):
            row.append(m1[i][j] + sign * m2[i][j])
        m3.append(row)
    return m3
