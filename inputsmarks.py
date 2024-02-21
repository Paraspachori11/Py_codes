#WAP to accept marks of 6 students and display them in sorted mannner

s1 = int(input("Enter marks of student 1 : "))
s2 = int(input("Enter marks of student 2 : "))
s3 = int(input("Enter marks of student 3 : "))
s4 = int(input("Enter marks of student 4 : "))
s5 = int(input("Enter marks of student 5 : "))
s6 = int(input("Enter marks of student 6 : "))

marks = [s1,s2,s3,s4,s5,s6]
marks.sort()
print(marks)