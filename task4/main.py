import argparse,os

parser = argparse.ArgumentParser()
parser.add_argument("-dir", "--dirpath" , help = "Use to get the path of directory",
                     type = str, default = "")

parser.add_argument("-file", "--file", help = "Use to get the file name",
					 default = "" , nargs = "+")

parser.add_argument("--write", help = "Use to write in a file",
					 action = "store_true")

parser.add_argument("-content", "--content", help = "Use to write text in a file", 
					 const = 1, nargs = "?", default = 0)

parser.add_argument("--read", help = "Use to write in a file",
					 action = "store_true")

args = parser.parse_args()


if not (args.dirpath == ""):
	if not(os.path.isdir(args.dirpath)):
		os.mkdir(args.dirpath)
	os.chdir(args.dirpath)
	for file_name in args.file:
		file = open(file_name,'w+')
		if(args.write):
			if not(args.content == 0):
				if(args.content == 1):
					args.content = str(args.content)
					args.content = "This is a default string"
				file.write(args.content + '\n')
				file.close()
			else:
				print("Enter a content using commad -content")
		if(args.read):
			for line in file:
				print (line + '\n') 
				
else:
	print("Enter a directory path using commad -dir path")
	