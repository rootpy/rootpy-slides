# test
from rootpy.io import root_open
from rootpy.tree import Tree, TreeModel
from rootpy.types import FloatCol
from random import gauss

class Event(TreeModel):
    variable = FloatCol(default=-1111)

with root_open('output.root', 'recreate'):
    tree = Tree(name='mytree', model=Event)
    for i in xrange(100):
        tree.variable = gauss(0, 1)
        tree.Fill()
    tree.Write()
