"""
Given the names and grades for each student in a Physics class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

>>>Input Format

The first line contains an integer, N, the number of students. 
The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains their grade.

>>>Constraints

There will always be one or more students having the second lowest grade.

>>>Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line. """

nlist = []
for i in range(int(raw_input())):          #Pre-written
        name = input()                 #Pre-written
        score = float(raw_input())         #Pre-written
        nlist.append([name,score])              # try : nlist.append([name], [score])
        nlist.sort(key = lambda x: x[1])
        
for m in range(0,len(nlist)):
    for n in range (0,1):
        print nlist[m][1]                  #Stuck here..
        
print nlist[::-1]
