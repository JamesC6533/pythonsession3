def fake_bin(x):

    result = ''

    for i in x:
        if int(i) >= 5:
            result += '1'

        else:
            result += '0'

    return result


def fake_bins(s):
    return ''.join('0' if char < '5' else '1' for char in s)


def friend(x):

    result = []

    for name in x:
        if len(name) == 4:
            result.append(name)

    return result


def friends(x):
    return [n for n in x if len(n) == 4]

