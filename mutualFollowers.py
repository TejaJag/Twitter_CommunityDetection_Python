import numpy as np
import csv

# loading the file containing only screen names into a list sn
with open('C:\\Users\\teja\\Documents\\1.MS\\1.Masters\\RA\\screennames_1_50.csv') as f:
    sn = [word.strip() for word in f]

lis = []
followers = [] # Contains the lists of list of followers of every user

myfile = open("matrix50.csv","w")
writer = csv.writer(myfile, lineterminator="\n")
with open('C:\\Users\\teja\\Documents\\1.MS\\1.Masters\\RA\\followersOnly_1_50.csv') as myfile:

    reader = csv.reader(myfile, lineterminator = "\n")
    for row in reader:
        lis = row  # converts a row i.e a single user followers from csv into list
        followers.append(lis)

#print followers
# to be optimized and then commented
compFol = []
follo = []
w = len(followers)
matrix = [[0 for x in range(w)] for y in range(w)]
for i in range(len(followers)-1):
    print "----", i
    follo = followers[i]
    matrix[i][i] = len(follo)
    if follo[0] == "N/A":
        for p in range(w):
            matrix[i][p] = "N/A"
            matrix[p][i] = "N/A"
        continue
    j=i+1
    for j in range(len(followers)):
        count = 0
        compFol = followers[j]
        if compFol[0] == "N/A":
            continue
        for k in range(len(follo)):
            if follo[k] in compFol:
                count = count + 1
        matrix[i][j] = count
        matrix[j][i] = count
if(followers[w-1][0] == "N/A"):
    for q in range(w):
        matrix[w-1][q] = "N/A"
else:
    matrix[w-1][w-1]=len(followers[w-1])
arr = np.array(matrix)
#print arr
#print arr.shape
arr = np.insert(arr, 0, sn, axis=1)

sn.insert(0,"--")


arr = np.insert(arr, 0, np.array(sn), axis=0)
# print arr

for row in arr:
    writer.writerow(row)


