########################################################################################################################
# Task
# You are given a string S and width w.
# Your task is to wrap the string into a paragraph of width w.
# Print the text wrapped paragraph.
########################################################################################################################

import textwrap

def wrap(string, max_width):
    para = textwrap.fill(string, max_width)
    return para

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
