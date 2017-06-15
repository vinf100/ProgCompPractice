import re

phrase = input('Input phrase')


def print_palindrome(line):
    text = re.sub('\W+', "", line.lower())
    rev_text = text[::-1]

    if text == rev_text:
        print('Yes, "{}"'.format(line))
    else:
        print('No, "{}"'.format(line))


print_palindrome(phrase)
