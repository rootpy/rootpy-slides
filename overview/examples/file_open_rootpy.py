# open a file with rootpy
from rootpy.io import root_open

myfile = root_open("file_does_not_exist.root")
print myfile
myfile.Get("something")
