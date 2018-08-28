import subprocess

#============================================================================================================
# - how to run an external command.
#============================================================================================================

# #Example no 1
# subprocess.call('python index.py', shell=True)

# #Example no 2
# subprocess.call("ls")



#============================================================================================================
# - how to get the output of executed commad.
#============================================================================================================

# #Example no 1
# process = subprocess.Popen("date", stdout=subprocess.PIPE)
# (output, err) = process.communicate()
# p_status = process.wait()
# print("Command output : ", output)
# print("Command exit status/return code : ", p_status)

# #Example no 2

# process = subprocess.Popen(['python', 'std_test.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# resulted_output = process.communicate()[0]

# print (resulted_output)

#============================================================================================================
# - how to wait for output if executed command is taking considerable time.
#============================================================================================================

# program = "gnome-calculator"
# process = subprocess.Popen(program)
# return_code = process.wait()
# print(return_code)


#============================================================================================================
# - how to run an external command in background (non-blocking call, 
#	which means the code goes ahead without waiting for output.)
#============================================================================================================

# subprocess.Popen(["python","index.py"])
# print("Subprocess run in the background")


#============================================================================================================
# - how to run two external commands in background (intensive commands that take considerable time) and then  
#   run a 3rd command but only when all previous commands (2 commands that were executed before) are completed.
#   i.e. 1st, 2nd command will run in background simultaneously but 3rd command will run only when 1st, 2nd 
#	commands are done  running.
#============================================================================================================


# commad1 = ['python','index.py']
# commad2 = ['python','index1.py']

# commands = [commad1,commad2]
# processes = [subprocess.Popen(cmd) for cmd in commands ]
# for process in processes:
#    process.wait()
# subprocess.Popen("ls")

#============================================================================================================
# - how to run a faulty external command and catch its error.
#============================================================================================================

# try:
# 	process = subprocess.Popen(["ls","/foo/bar"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# 	(out,err) = process.communicate()

# 	if (process.returncode == 0):
# 		print("command succeeded, returned: %s"% (str(out)))
# 	else:
# 		print("command failed\nexit-code=%d\nerror = %s \n"% (process.returncode, str(err)))
# except OSError as e:
#     sys.exit("failed to execute program  %s" % (str(e)))

#============================================================================================================
# - - how to show live output of external command on console (using python). 
#============================================================================================================
# def run(command):
#     process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
#     while True:
#         line = process.stdout.readline().rstrip()
#         if not line:
#             break
#         yield line


# if __name__ == "__main__":
#     for path in run("ping -c 5 google.com"):
#         print (path)
