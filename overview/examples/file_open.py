"""
ROOT is unable to open the file of course and emits an error message but an
exception is not raised at this point leading to (sometimes difficult to
intepret) issues downstream:
"""
from ROOT import TFile

myfile = TFile.Open("file_does_not_exist.root")
print myfile
myfile.Get("something")
