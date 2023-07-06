def solution(N, A):
    counters = [0] * N
    max_counter = 0
    last_max_counter = 0

    for x in A:
        if 1 <= x <= N:
            if counters[x - 1] < last_max_counter:
                counters[x - 1] = last_max_counter
            counters[x - 1] += 1
            if counters[x - 1] > max_counter:
                max_counter = counters[x - 1]
        elif x == N + 1:
            last_max_counter = max_counter

    for i in range(N):
        if counters[i] < last_max_counter:
            counters[i] = last_max_counter

    return counters


N = 5
A = [3, 4, 4, 6, 1, 4, 4]
result = solution(N, A)
print(result)


def solution(N, A):
    counters = [0] * N
    max_counter = 0
    current_max = 0

    for x in A:
        if 1 <= x <= N:
            counters[x - 1] = max(counters[x - 1], current_max)
            counters[x - 1] += 1
            max_counter = max(max_counter, counters[x - 1])
        elif x == N + 1:
            current_max = max_counter

    for i in range(N):
        counters[i] = max(counters[i], current_max)

    return counters


N = 5
A = [3, 4, 4, 6, 1, 4, 4]
result = solution(N, A)
print(result)




