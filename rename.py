#WAP to rename a file to "renamed_by_python.txt"

import os #with the help of this module the 'oldfile' would be deleted

oldfile = 'renamethisfile.txt'
newfile = "renamed_by_python.txt"
with open(oldfile) as f:
    content = f.read()
with open(newfile,'w') as f:
    f.write(content)

os.remove(oldfile)