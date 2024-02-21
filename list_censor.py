# repeat replacer_#.py for alist of such words to be censored

words = ["gadhe","motherfucker","bitch"]

with open('system.txt') as f:
    a = f.read()

for word in words:
    a = a.replace(word,'@$%^&*!')
with open('system.txt','w') as f:
    f.write(a)
