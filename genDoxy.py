import os

def isCFile(path):
	startOfExt = path.rfind(".");
	fileExt = path[startOfExt:];

	if(fileExt == ".cpp" or fileExt == ".c" or fileExt == ".h"):
		return True;

	else:
		return False;


def generateDoxygen():
	path = "";
	while( path != "q" ):
		path = input("Please enter absolute path to target directory/file (Enter q to quit): ");

		if( os.path.isfile(path) ):
			if(isCFile(path)):
				parseFile(path);

		elif(os.path.isdir(path) ):
			if(path[-1] == "/"):
				parseDir(path[:-1])

			else:
				parseDir(path);

		elif( path == "q" ):
			print("Exiting...");

		else:
			print("Error finding/opening file or directory");


def parseDir(filePath):
	for(dirPath, dirNames, fileNames) in os.walk(filePath):
		for fileName in fileNames:
			if(isCFile(fileName)):
				parseFile(dirPath + "/" + fileName);


def parseFile(path):
	


generateDoxygen();
