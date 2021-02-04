#!/usr/bin/python3
import urllib
import requests
import sys
from datetime import datetime

def getTime():
	now = datetime.now()
	dateAndTime = now.strftime("%m/%d/%Y %H:%M:%S")
	return dateAndTime



def connect(host='http://google.com'):
    try:
    	requests.get('https://www.google.com/').status_code
    	return True
    except:
    	return False

def main(): 
	x = datetime.now()
	today = x.strftime("%B,%d")

	file = open( today + ".txt", 'a')

	if connect():
		file.write("connected  ")
	else:
		file.write("no internet!  ")

	file.write(getTime())
	file.write("\n")
	file.close()
	
main()