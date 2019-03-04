import os

def parseDir(filePath):
	# print(filePath);
	for(dirPath, dirNames, fileNames) in os.walk(filePath):
		# print("Dir Path: ", dirPath);
		# print("Dir Name: ", dirNames);
		# print("File Names: ", fileNames);

def generateDoxygen():
	path = "";
	while(path != "q"):
		path = input("Please enter absolute path to target directory/file (Enter q to quit): ");
		parseDir(path);

generateDoxygen();
