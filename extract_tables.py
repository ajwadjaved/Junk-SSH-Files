#!/usr/bin/python3

#for a more efficient way to read large files:
#https://stackoverflow.com/questions/47927039/reading-a-file-until-a-specific-character-in-python

import glob

path = "/mnt/mydrive/Workspace/arxiv/explore/0001/Sample1/*.tex"

for filename in glob.glob(path):
    print(glob.glob(path))
    with open(filename, "r") as f, open("TexTables.tex", "w") as g:
        extract = False
        for line in f:
            if "\\begin{table}" in line:
                extract = True
            if extract:
                g.write(line)
            if "\\end{table}" in line:
                extract = False
                g.write("\n")

