def shortest_word_length(string):

    words = string.split()  # Split the string into a list of words
    shortest_length = min(len(word) for word in words)  # Find the minimum length using a generator expression
    
    return shortest_length


def find_short(s):
    return min(len(w) for w in s.split())
