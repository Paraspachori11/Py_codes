#WAP to check whether a file is identical & makes the content of another file

with open('this.txt') as f:
    with open('copy.txt') as g:   #can also check for system.txt
        if f.read() == g.read():
            print("yes the files are identical")
        else:
            print("Not")