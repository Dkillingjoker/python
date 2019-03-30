"""
You are given a string  and width . 
Your task is to wrap the string into a paragraph of width .

>>Input Format

The first line contains a string, S. 
The second line contains the width, w.


>>Output Format

Print the text wrapped paragraph.

"""

import textwrap

def wrap(string, max_width):
    a = textwrap.wrap(string, width=max_width)
    b = "\n".join(a)
    return b

if __name__ == '__main__':                                      #Pre-written call
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print result


# All test cases passed!