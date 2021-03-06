# test
from ROOT import TTree, TFile
from array import array
from random import gauss

output_file = TFile.Open('output.root', 'recreate')
variable = array('f', [0.])
tree = TTree('mytree', '')
tree.Branch('variable', variable, 'variable/F')

for i in xrange(100):
    variable[0] = gauss(0, 1)
    tree.Fill()

tree.Write()
output_file.Close()
