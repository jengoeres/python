import os

directory = input("Please enter what directory you want to save your file to: ")
filename = input("Please enter your file name: ")
name = input("Please enter your name: ")
address = input("Please enter your address: ")
phoneNumber = input("Please enter your phone number: ")

path = directory+filename
content = name, address, phoneNumber

def createFile(path):
	f = open(path, "x")

createFile(path)

with open(path, 'w') as fileHandle: #open file for writing
	fileHandle.write(str(content)) #write data to file
with open(path, 'r') as fileHandle: #open same file for reading
	data = fileHandle.read() #read data from the file
	print("The information you entered is:")
	print(data)
