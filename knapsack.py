#!/usr/bin/env python3
# 11-28-16
# RC

# W: max weight capacity of bag
# w: weight
# N: total items in pool
# n: current item count

import sys      #use for command line args

with open(sys.argv[1], 'r') as f:
    first = True    #used to limit for first run
    items = []      #makes an indexable empty list for items, subformat: (value, weight)

    for line in f:      
        if (first):                     #turns false after one iteration
            lineList = line.strip().split()     #strip takes out the spaces on left and right, split puts separate elements into list
            W = int(lineList[0])                #sets W equal to 1st element in list (W is max weight capacity of sack)
            N = int(lineList[1])                #sets N equal to 2nd element in list (N is the total # of items in pool)
            first = False                       #this portion is now done
        else:
            lineList = line.strip().split()     #starts on 2nd line in text file
            lineList[0] = int(lineList[0])      # 0 = value         
            lineList[1] = int(lineList[1])      # 1 = weight
            items.append(lineList)              #append the current iteration's list to the master list of item values & weights

items.sort(key=lambda x: x[1])      #SORT the master list of items by weight (CRUCIAL Step)
#-----------------------------------------------------------------------------------------

#Create list for table of max values per weight and available items, initialize to 0
K = [[0 for x in range(W+1)] for y in range(N+1)]

for n in range(1, N+1):     # n specifies # of items (rows)
    for w in range(1, W+1): # w specifies amount of weight (columns)
        #if(n==0 or w==0):  # set "0" row & column to 0
        #   K[n][w] = 0

        if(items[n-1][1] > w):
            K[n][w] = K[n-1][w]

        else:
            K[n][w] = max(K[n-1][w], items[n-1][0] + K[n-1][w - items[n-1][1]])
        
#print max Total Value
print(K[N][W])
