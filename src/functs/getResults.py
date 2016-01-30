import numpy as np
from os import listdir
from os.path import isfile, join
from stabFuncts import getITF

resPath = "Videos/"
onlyfiles = [f for f in listdir(resPath) if isfile(join(resPath, f))]
onlyfiles.sort()
maxlength = max(len(s) for s in onlyfiles)
onlyfilesext = [f.ljust(maxlength, ' ') for f in onlyfiles]

names = np.array(onlyfilesext)
#print onlyfiles
#print names

# compute ITF
itf = []
for vid in onlyfiles:
    itf.append(str(getITF(resPath+vid)))
itf = np.array(itf)

res =  np.column_stack((names, itf))
np.savetxt("res.txt", res, delimiter=" ", fmt="%s")
