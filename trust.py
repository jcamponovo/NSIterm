import os
g = open("trust.sh","w")
g.write("#!/bin/bash\n")
fichier=[] 
for root, dirs, files in os.walk(os.getcwd()): 
    for i in files: 
        fichier.append(os.path.join(root, i)) 
for f in fichier:
    if f[-6:] == ".ipynb":
        # os.popen("jupyter trust {}".format(f))
        # print("jupyter trust {}".format(f))
        g.write("jupyter trust {}\n".format(f))
g.close()
