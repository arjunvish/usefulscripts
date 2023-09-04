#!/usr/bin/python3
#Script to go through discographies and rename folder names and file names according to a convention
import os
import re

curr = './'
for root, dirs, files in os.walk(curr):
  #for each directory
  for subdir in dirs:
    #for each mp3 file in the directory
    for fname in os.listdir(subdir):
      #Rename `[0-9][0-9] - name.mp3` by `[0-9][0-9] name.mp3`
      if fname.endswith('.mp3'):
        num = re.search(r'([0-9][0-9] )- ', fname)
        fname2 = re.sub(r'[0-9][0-9] - ', num.group(1), fname)
        os.rename(os.path.join(subdir, fname), os.path.join(subdir, fname2))
    #Rename `year name (blah)` to `year name`
    #subpref = re.search(r'([0-9][0-9][0-9][0-9] .*?)\(', subdir)
    #subdir2 = re.sub(r'.*', subpref.group(1), subdir)
    #os.rename(subdir, subdir2)

