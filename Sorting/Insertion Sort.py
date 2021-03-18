"""
Created on Tue Sep 29 20:46:21 2020

@author: Ayush Varshney

"""

def insertionSort(arr):
   for i in range(1, len(arr)):
      key = arr[i]
      j = i-1
      while j >=0 and key < arr[j]:
         arr[j+1] = arr[j]
         j -= 1
      arr[j+1] = key

arr = [3,7,5,8,4,9]
insertionSort(arr)
print ("The sorted array is:")
for i in range(len(arr)):
   print(arr[i],end=" ")