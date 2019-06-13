import sys

n_cases = int(sys.stdin.readline())

for i in range(n_cases):
    f_line = sys.stdin.readline().split()
    n_towns = int(f_line[0])
    id_town = int(f_line[1])
    n_employees = int(sys.stdin.readline())
    A = [0] * n_towns
    B = [[]] * n_towns

    for j in range(n_employees):
        s_line = sys.stdin.readline().split()
        hometown = int(s_line[0]) - 1
        n_passengers = int(s_line[1])
        A[hometown] += 1
        if len(B[hometown]) == 0:
            B[hometown] = [n_passengers]
        else:
            B[hometown].append(n_passengers)

    string = "#" + str(i)
    print "Case", string
    S = []
    for j in range(n_towns - 1):
        if j != id_town:
            suma = sum(B[j])
            if suma < A[j]:
                print "Impossible"
                break
            B[i].sort(reverse=True)
            m = 0
            acc = 0
            while acc < suma:
                m += 1
                acc += B[m - 1]
                S.append(m)
        else:
            S.append(0)
    print S