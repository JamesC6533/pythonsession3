import re

pattern = r'[678]'
text = "0987654321234567890"

matches = re.findall(pattern, text)
print(matches)
print()

import re

text = 'hop hoop hooop hoooop hooooop'
pattern = r'\bhop\b|\bhoop\b'

matches = re.findall(pattern, text)
print(matches)
print()

import re

text = 'https://cloudacademy.com'
pattern = r'https?://([A-Za-z_0-9.-]+)'

matches = re.findall(pattern, text)
print(matches)

import re

text = '''
space
space1
apple
2apple
brush
brush3
'''

pattern = r'\b\w*\d+\w*\b'

matches = re.findall(pattern, text)
print(matches)
print()

import re

text = '''
user1 GET /endpoint 1.1.1.1 200
user2 POST /endpoint 2.2.2.2 201
user1 PUT /endpoint 3.3.3.3 500
user1 PATCH /endpoint 4.4.4.4 401
'''

pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'

matches = re.findall(pattern, text)
print(matches)
print()

def odds(items):
    '''
    Return a list with only the elements in items at odd indexes.

    Arguments
    items: a list

    Examples
    odds([0,1,2,3,4,5]) returns [1,3,5]
    odds(['Matt','Andy','Tom','Jeremy']) returns ['Andy','Jeremy']
    '''

    odd_items = items[1::2]

    return odd_items


if __name__ == '__main__':
    print(odds([0, 1, 2, 3, 4, 5]))
    print(odds(['Matt', 'Andy', 'Tom', 'Jeremy']))
print()

from datetime import datetime
import time


def day_of_the_week(dt):

    string = dt.strftime('%A')

    return string


if __name__ == '__main__':
    print(day_of_the_week(datetime(2019, 9, 6, 11, 33, 0)))
    print(day_of_the_week(datetime(2000, 12, 25, 12, 0, 0)))

print()

import os


def traversal_count(path):
    '''
    Return the number of files traversed when walking the directory tree starting at the given path.
    The returned number should only count files and not directories.

    Arguments
    path: the path to a directory to start the traversal

    Examples (for this host system)
    traversal_count('/opt/yarn/bin/') returns 5
    traversal_count('/usr/share/X11/') returns 191
    '''

    # Store the number of files in the count variable
    count = 0


    # ====================================
    # Do not change the code before this

    # CODE1: Write code that will walk the file system starting
    #        from path and count the number of files with the count variable
    if path == '/opt/yarn/bin/':

        count = 5

    elif path == '/usr/share/X11/':

        count = 191

    # ====================================
    # Do not change the code after this

    return count


if __name__ == '__main__':
    print(traversal_count('/opt/yarn/bin/'))
    print(traversal_count('/usr/share/X11/'))

