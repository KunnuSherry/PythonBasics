# This program is to print all the files in a directory

import pathlib
res=[]
path  = pathlib.Path("./Basic Programs")
for entry in path.iterdir():
    res.append(entry)
print(res)