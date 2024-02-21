#WAP to mine a log file(here log.txt) and find out whether it contains 'python' 

with open('log.txt') as f:
    content = f.read()

if 'python' in content.lower():
    print("YES it contains PYTHON")
else:
     print("NO it didn't contains PYTHON")