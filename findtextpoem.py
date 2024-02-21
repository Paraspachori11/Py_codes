#WAP to read the text from the file 'poem.txt' and find out 'whether it contains the word 'twinkle'

f = open('poems.txt')
a = f.read()
print(a)
if 'twinkle' in a:
    print("yes it contains the word TWINKLE")
else:
    print("no it doesn't contains the word TWINKLE")
f.close()