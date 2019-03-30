"""
You have a record of N students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters some integer N followed by the names and marks for N students. You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.

>>>Input Format

The first line contains the integer N, the number of students. The next N lines contains the name and marks obtained by that student separated by a space. The final line contains the name of a particular student previously listed.

>>>Output Format

Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.
"""

if __name__ == '__main__':                         #Pre-written
    n = int(raw_input())
    student_marks = {}
    for i in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()                          

    n=0                                             #code
    s=0
    x = student_marks[query_name]
    for n in range (0,len(x)):
        s += x[n]
    avg = s / len(x)
    print ('%.2f' % avg)


    " All test cases valid!"
