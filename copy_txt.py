#WAP to make a copy of a file 'this.txt'
name = input("Enter the name of clone file\n")

with open('this.txt') as f:
    a = f.read()

with open(f"{name}.txt",'w') as f:
    f.write(a)
