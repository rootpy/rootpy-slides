from ROOT import TFile

myfile = TFile.Open("file_does_not_exist.root")
print myfile
myfile.Get("something")
