# test
from rootpy.tree import Tree
from rootpy.io import root_open
from random import gauss

f = root_open("test.root", "recreate")

tree = Tree("test")
tree.create_branches(
        {'some_float': 'F',
         'some_int': 'I'})

for i in xrange(10000):
    tree.some_float = gauss(.5, 1.)
    tree.some_int = i
    tree.fill()
tree.write()
f.close()
