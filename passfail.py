#WAP to find out whether a student is pass or fail , if it requires total 40% and atleast 33% in each subject to pass . Assume 3 subjects  and take marks as an input from the user.

from turtle import goto


s1 = int(input("Enter marks of subject 1 : "))
s2 = int(input("Enter marks of subject 2 : "))
s3 = int(input("Enter marks of subject 3 : "))

Each_sub_mark = 70
a = int(Each_sub_mark)

#percentage of each subject 
ps1 = int(s1*100/a)
ps2 = int(s2*100/a)
ps3 = int(s3*100/a)

#total percentage

Total = 210
c = int(Total)
Studentper = int((s1+s2+s3)*100/c)

#display
print("MAX marks of each subject",a)
print("Total MAX marks ",c)
print("percentage of subject 1 :",ps1)
print("percentage of subject 2 :",ps2)
print("percentage of subject 3 :",ps3)
print("Overall percentage",Studentper)

#to print pass/fail

if(Studentper>=40 and ps1>=33 and ps2>= 33 and ps3>=33):
    print("PASS")
else :
    print("FAIL" )
