# creating histograms
from rootpy.plotting import Hist3D

# variable width bins
hist3d = Hist3D([0, 3, 10, 100], [2.3, 4.2, 5.8, 10, 20, 25.5], [-100, 0, 20])
# easy to mix variable and fixed width bins with rootpy
hist3d = Hist3D(3, 0, 5, [2.3, 4.2, 5.8, 10, 20, 25.5], [-100, 0, 20])
