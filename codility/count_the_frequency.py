def solution(S):
    S = S.split()
    result = {}
    for i in S:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result


S = "This is a test sentence, a sentence used to test"
result = solution(S)
print(result)


def solution(L, W):
    return L * W


L = 5
W = 2
result = solution(L, W)
print(result)