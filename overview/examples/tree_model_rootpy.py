# test
from rootpy.tree import Tree
from rootpy.tree import TreeModel
from rootpy.tree import FloatCol
from rootpy.tree import IntCol

class FourVect(TreeModel):
    eta = FloatCol(default=-1111.)
    phi = FloatCol(default=-1111.)
    pt = FloatCol()
    m = FloatCol()

class Tau(FourVect):
    numtrack = IntCol()

class Event(Tau.prefix('tau1_'),
            Tau.prefix('tau2_')):
    event_number = IntCol()
    run_number = IntCol()

# tree = Tree('data', model=Event)
print Event
