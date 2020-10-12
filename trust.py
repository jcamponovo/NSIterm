import os
g = open("trust.sh","w")
g.write("#!/bin/bash\n")
fichier=[]
acopier = []
base = []
for root, dirs, files in os.walk(os.getcwd()): 
    for i in files: 
        fichier.append(os.path.join(root, i))
    if root[-8:-3] == "Cours":
        for i in files: 
            acopier.append((os.path.join(root, i),i))
    if root[-4:] == "2020":
        for i in dirs: 
            base.append(os.path.join(root, i))
for f in fichier:
    if f[-6:] == ".ipynb":
        # os.popen("jupyter trust {}".format(f))
        # print("jupyter trust {}".format(f))
        g.write("jupyter trust {}\n".format(f))
for i in acopier:
    for j in base:
        if not os.path.exists(os.path.join(j,i[1])):
            g.write("cp {} {}\n".format(i[0],os.path.join(j,i[1])))

g.close()
