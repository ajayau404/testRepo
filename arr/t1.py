#!/usr/bin/env python

import sys, os, time, json
import array

def main():
	arr = array.array('i', [1,2,3])
	print(arr, len(arr))
	for i in range(len(arr)):
		print(arr[i], end=',')
	print("\r")
	arr.append(4)
	print(arr, len(arr))
	arr.insert(2,5)
	print(arr, len(arr))
	print(arr.pop(2))
	print(arr, len(arr))
	arr.append(1)
	print(arr, len(arr))
	arr.remove(1)
	print(arr, len(arr))
	print(arr.index(1))
if __name__ == "__main__":
	main()