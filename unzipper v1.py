''' This code is to unzip multiple files in a directory '''

import os
import zipfile
import contextlib
from_dir = raw_input("Enter the Directory where zip files are : ")
to_dir   = raw_input("Enter the Directory where u want to unzip : ")

list_dir = os.listdir(from_dir)
os.chdir(from_dir)
print 'Extracting.'
for i in range(0,len(list_dir)):
    try :
        with contextlib.closing(zipfile.ZipFile(list_dir[i],"r")) as z:
            z.extractall(to_dir)
            print (i*100)/len(list_dir),'% complete.' 
    except :
        print list_dir[i],"-> Bad ZipFile."
        i=i+1

print 'Done.'
