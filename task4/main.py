import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("dir", help="Use to get the path of directory")

parser.add_argument("-file", help="Use to get the file name",
                    default=list() , nargs="+")

parser.add_argument("-content", help="Use to write text in a file", 
                    nargs="?", type=str, default='my default writing content.')

parser.add_argument("--write", help="Use to write in a file",
                    action="store_true")

parser.add_argument("--read", help="Use to read in a file",
                    action="store_true")

args = parser.parse_args()

if __name__ == '__main__':

  print(args.__dict__, end='\n\n') 

  args.dir = os.path.abspath(args.dir)
  if not os.path.isdir(args.dir):
    os.mkdir(args.dir)

  if (not args.file and args.read):
    for file_name in os.listdir(args.dir):
      file = open(os.path.join(args.dir, file_name), 'r')
      
      content = file.read().strip('\n')
      if not content:
        content = 'none found'

      print ("%s: %s" % (file_name, content))
      file.close

  elif (args.file and args.read):
    for filename in args.file:
      fullname = os.path.abspath(os.path.join(args.dir, filename))

      if os.path.isfile(fullname):
        file = open(fullname, 'r')
        content = file.read()
        file.close()
        print('%s: %s' % (filename, content))
      else:
        print('%s: Not found.' % (filename))


  if args.write:

    if not args.file:
      print('No file was specified for writing...')

    for file_name in args.file:
      fullname = os.path.abspath(os.path.join(args.dir, file_name))

      if not args.content:
        args.content = 'default string of content is here.'

      file = open(fullname, 'w')
      file.write(args.content + '\n')
      file.close()
      print('Content written to file: %s' % (file_name))