#WAP to find out the line number where python is present from (log.txt)

content = True
i = 1
with open('log.txt') as f:
    while content:
        content = f.readline()
        if 'python' in content.lower():
           print(content,end='')
           print(f"python is presnet in line {i} ")
        i+=1
   