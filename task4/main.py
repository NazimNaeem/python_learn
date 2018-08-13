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
	if(args.file == "" and args.read):
		for file_name in os.listdir(args.dirpath):
			file = open(file_name,'r')
			print (" from {} : content : {} ".format(file_name,file.readline()))
			file.close 
	elif(args.file == "" and args.write):
		print("Enter a file name using command -file filename")
			

	for file_name in args.file:
		if not(os.path.isfile(file_name)):
			open(file_name,'w+')
		if(args.write):
			file = open(file_name,'w+')
			if not(args.content == 0):
				if(args.content == 1):
					args.content = str(args.content)
					args.content = "This is a default string"
				file.write(args.content + '\n')
				file.close()
			else:
				print("Enter a content using commad -content")
		if(args.read):
			file = open(file_name,'r')
			for content_in_file in file:
				print (" from {} : content : {} ".format(file_name,content_in_file))
				file.close 
				
else:
	print("Enter a directory path using commad -dir path")
	