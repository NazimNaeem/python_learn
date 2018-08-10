# Task #1
# Write a function to fetch all files in a directory.Keep them in a list and sort the list alphabaticaly and add _edited 
# with each file name and create new subfolder and store these newly name files in that folder 

# ===================================================================================
# Task #2
# open the edited files and write the its name as its content and then close it.
# there must be a new line at the end of file.

import os
def subdirs(path, subfolder, extension):
	"""Yield directory names not starting with '.' under given path."""
	if(os.path.isdir(path)):

		files = [os.path.splitext(file) for file in os.listdir(path) if not file.startswith('.') if file.endswith(extension)]
	
		file_name=[name_part[0] for name_part in files]
		file_name.sort(key=lambda part: float(part[1:]))
		files = ['%s_edited%s' % (item,extension) for item in file_name]
		
		os.chdir(path)
		path=os.path.join(path,subfolder)
		if not(os.path.isdir(path)):

			os.mkdir(subfolder)
			os.chdir(path)
			for file_name in files:
				file=open(file_name,'w+')
				file.write(file_name +'\n')
				file.close()
		else:
			print("SubDirectory Already exist")
	else:
		print("Directory Does not exist")

sub_folder=input("Enter the name of folder :")
ext=input("Enter the extension :")
subdirs("/home/ebryx/Desktop/python/Task1/file", sub_folder,ext)


