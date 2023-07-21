from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def sort012(arr, n) :

    low = cur = 0
    high = n - 1
    while(cur <= high) :
        if(arr[cur] == 0) :
            arr[low], arr[cur] = arr[cur], arr[low]
            low += 1
            cur += 1
        elif(arr[cur] == 1) :
            cur += 1
        elif(arr[cur] == 2) :
            arr[cur], arr[high] = arr[high], arr[cur]
            high -= 1
    


#taking inpit using fast I/O
def takeInput() :
	n = int(input().strip())

	if n == 0 :
		return list(), 0

	arr = list(map(int, stdin.readline().strip().split(" ")))

	return arr, n



def printAnswer(arr, n) :
    
    for i in range(n) :
        
        print(arr[i],end=" ")
        
    print()
    
#main

t = int(input().strip())
for i in range(t) :

    arr, n= takeInput()
    sort012(arr, n)
    printAnswer(arr, n)
