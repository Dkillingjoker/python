"""
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

>>Input Format 
The first line contains a string consisting of space separated words.

>>Output Format 
Print the formatted string as explained above.

"""

def split_and_join(line):
    s = line.split(" ")
    s = "-".join(s)
    return s


if __name__ == '__main__':              #pre-written function call
    line = raw_input()
    result = split_and_join(line)
    print result


# All Test Cases passed!