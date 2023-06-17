def string_fun(string):
    details = (
        string.isalpha(),                      # Check if the string contains only alphabet characters
        string.endswith('!'),                  # Check if the string ends with an exclamation mark
        string.replace(' ', '-')               # Replace all spaces with hyphens
    )
    return details

if __name__ == '__main__':
    print(string_fun('Hello World!'))
    print(string_fun('ThisIsAChallenge'))

def list_uniqueness(the_list):

    dictionary = {
        'list_length': len(the_list),
        'unique_items': len(set(the_list))
    }
    return dictionary

# Rest of the code remains the same
if __name__ == '__main__':
    l = [1, 2, 2, 4]
    dictionary = list_uniqueness(l)
    print(dictionary['list_length'])
    print(dictionary['unique_items'])


def append(the_list, item):
    the_list.append(item)

# Rest of the code remains the same
if __name__ == '__main__':
    l = [1, 2, 3]
    append(l, 4)
    print(l)
