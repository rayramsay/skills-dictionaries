"""Dictionaries Assessment

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    word_count = {}

    words = phrase.split(' ')  # hypothetically I could have chained .lower()
    for word in words:         # before .split(), but that screws up the test
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """

    melon_prices = {'Watermelon': 2.95, 'Cantaloupe': 2.50, 'Musk': 3.25,
                    'Christmas': 14.25}

    if melon_name in melon_prices:
        return melon_prices[melon_name]
    else:
        return "No price found"


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
    """

    word_dict = {}
    word_length = []

    for word in words:
        if len(word) in word_dict:
            word_dict[len(word)] = word_dict[len(word)] + [word]
        else:
            word_dict[len(word)] = [word]

    for key, value in word_dict.iteritems():
        word_length.append((key, sorted(value)))

    return word_length


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

    translated_words = []
    pirate_dict = {'sir': 'matey', 'hotel': 'fleabag inn', 'student': 'swabbie',
                   'man': 'matey', 'professor': 'foul blaggart',
                   'restaurant': 'galley', 'your': 'yer', 'excuse': 'arr',
                   'students': 'swabbies', 'are': 'be', 'restroom': 'head',
                   'my': 'me', 'is': 'be'}

    words = phrase.split(' ')
    for word in words:
        if word in pirate_dict:
            translated_words.append(pirate_dict[word])
        else:
            translated_words.append(word)

    phrase = (' ').join(translated_words)

    return phrase


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    # This kind of works, except in the ways it does Not.

    # I'm sort of thinking about this like it's a network graph, in that the
    # words are nodes that share edges on the basis of the last letter of one
    # word being the first letter of another. I have to traverse this graph
    # given the starting location, and when there's more than one edge, I don't
    # get to choose between them; I have to use the one that leads to the next
    # word in the list. Also, once I pass through a node, I can't go through it
    # again.

    # Tragically, I don't actually know any strategies for traversing graphs, so
    # this conceptualization has not been especially helpful.

    names_dict = {}

    # Get all the words in the dictionary as keys with empty lists for values.
    for name in names:
        names_dict[name] = []

    # For each word, check to see if any other word starts with the same letter
    # the word ends with, in which case it should be added to the values for
    # that key.
    for name in names:
        index = 0
        while index < len(names):
            if name.startswith(names[index][-1]):
                names_dict[names[index]] = names_dict[names[index]] + [name]
            index += 1

    # Start the chain with the first word in the list.
    chain = [names[0]]

    # See if the last word in the chain has a value that's first item is also a
    # key in the dictionary; if so, add that item to the chain and delete the
    # key-value pair so you can't use it again. If not, look at the next item.
    index = 0
    while True:
        try:
            if names_dict[chain[-1]][index] in names_dict:
                chain += [names_dict.pop(chain[-1])[index]]
            else:
                index += 1  # you'll notice this doesn't go back down, so it
                            # passes the doctest but isn't a good solution
        except IndexError:
            break           # this is also not a good way to leave

    return chain

    # I want to solve this for all cases but I'm over the time limit.

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
