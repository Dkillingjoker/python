"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given 'n' scores. 
Store them in a list and find the score of the runner-up.

Input Format

The first line contains 'n'. The second line contains an array A[]  of 'n' integers each separated by a space.

Output Format

Print the runner-up score. 
"""

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())  #Pre-written

    x = max(arr)
    r = arr[::-1]
    for a in r:
        if a == x:
            arr.remove(a)
                    
    y = max(arr)    
    print y        
        

# All test cases passed !

