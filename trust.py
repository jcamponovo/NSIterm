import os

liste = os.listdir()
for f in liste:
    if f[-6:] == ".ipynb":
        os.popen("jupyter trust '{}'".format(f))
