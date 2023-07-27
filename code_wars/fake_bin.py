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