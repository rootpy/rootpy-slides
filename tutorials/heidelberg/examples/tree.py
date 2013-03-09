from rootpy.io import open
from rootpy.tree import Tree, TreeModel
from rootpy.types import FloatCol, IntCol
import random

class Model(TreeModel):
    x = FloatCol(default=-1.)
    y = FloatCol()
    i = IntCol()

f = open('test.root', 'recreate')
tree = Tree(name='test', model=Model)

for i in xrange(100):
    tree.x = random.gauss(4, 3)
    tree.y = random.gauss(2, 3)
    tree.i = i
    tree.fill()

tree.write()
f.close()
