#!/usr/bin/env python

import sys, os, time, json

def main():

	numElem = 3
	elemStr = "1 0 0"

	elemList = elemStr.split(" ")	
	val = 0
	count = 0
	for eachElem in elemList[::-1]:
		val += (int(eachElem) ^ 1) * pow(2, count)
		count +=1
	print val


if __name__ == "__main__":
	main()