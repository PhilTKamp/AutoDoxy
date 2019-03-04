import os

def parseDir(filePath):
	# print(filePath);
	for(dirPath, dirNames, fileNames) in os.walk(filePath):
		# print("Dir Path: ", dirPath);
		# print("Dir Name: ", dirNames);
		# print("File Names: ", fileNames);
		for fileName in fileNames:
			parseFile(dirPath + "/" + fileName);


def parseFile(path):
	print("Parsing file: ", path);



def generateDoxygen():
	path = "";
	while( path != "q" ):
		path = input("Please enter absolute path to target directory/file (Enter q to quit): ");
		if( os.path.isfile(path) ):
			parseFile(path);
		elif(os.path.isdir(path) ):
			if(path[-1] == "/"):
				parseDir(path[:-1])
			else:
				parseDir(path)
		elif( path == "q" ):
			print("Exiting...")
		else:
			print("Error finding/opening file or directory");

generateDoxygen();
