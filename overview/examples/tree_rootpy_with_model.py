# test
from rootpy.tree import Tree, TreeModel
from rootpy.tree import FloatCol, IntCol
from rootpy.io import root_open
from random import gauss

f = root_open("test.root", "recreate")

class Model(TreeModel):
    some_float = FloatCol()
    some_int = IntCol()

tree = Tree("test", model=Model)

for i in xrange(10000):
    tree.some_float = gauss(.5, 1.)
    tree.some_int = i
    tree.fill()
tree.write()
f.close()
