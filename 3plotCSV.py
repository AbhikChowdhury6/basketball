import matplotlib.pyplot as plt
import sys
import os
import fnmatch

directory = sys.argv[1]
sensorType = sys.argv[2]
firstType = sys.argv[3]
secondType = sys.argv[4]
thirdType = sys.argv[5]

for file in os.listdir(directory):
    if fnmatch.fnmatch(file,'*' + sensorType + '*'):
        fileName = file



with open(directory + fileName, 'r') as myfile:
    raw=myfile.read().replace('\n', '')


sets = raw.split(",")
sets.pop()
print("number of data poits: " + str(len(s)))

firsts = []
seconds = []
thirds = []

for s in sets:
    numList = S[1:-1]
    firsts.append(numList[0])
    seconds.append(numList[1])
    thirds.append(numList[2])



#print s
plt.plot(firsts)
plt.plot(seconds)
plt.plot(thirds)
plt.ylabel('magnitude')
plt.ylabel('samples')
plt.legend([firstType, secondType, thirdType], loc='upper left')
plt.show()