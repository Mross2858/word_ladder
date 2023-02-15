#!/bin/python3

from collections import deque
import copy


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny',
    'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty'
    , 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    with open(dictionary_file, 'r') as f:
        text = f.read()
    dictionary = text.split()
    stack = []
    stack.append(start_word)
    queue = deque()
    queue.append(stack)
    if start_word == end_word:
        return stack
    while len(queue) != 0:
        working_queue = queue.popleft()
        cur_stack = copy.copy(dictionary)
        for i in cur_stack:
            if _adjacent(i, working_queue[-1]) is True:
                if i == end_word:
                    working_queue.append(i)
                    return working_queue
                else:
                    new_stack = copy.copy(working_queue)
                    new_stack.append(i)
                    queue.append(new_stack)
                    dictionary.remove(i)
    return None


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    # queue = collections.deque(ladder)
    # tck = collections.deque([ladder[i + 1] for i in range(len(ladder) - 1)])
    # while queue and stack:
    #     word1 = queue.popleft()
    #     word2 = queue.pop()
    #     if not _adjacent(word1, word2):
    #         return False
    # return True
    if ladder == [] or ladder is None:
        return False
    if len(ladder) == 1:
        return True
    for i in range(len(ladder)-1):
        if not _adjacent(ladder[i], ladder[i + 1]):
            return False
    return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''

    if len(word1) == len(word2):
        count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count += 1
        if count > 1:
            return False
        elif count == 0:
            return False
        else:
            return True
    else:
        return False
