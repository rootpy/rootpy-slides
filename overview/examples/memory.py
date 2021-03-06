# test
from ROOT import TCanvas, TH1D

def make_plot():
    canvas = TCanvas('plot', 'plot',
                     700, 500)
    hist = TH1D('hist', 'plot',
                10, -3, 3)
    hist.FillRandom('gaus')
    hist.Draw()
    return canvas

canvas = make_plot()
# empty canvas since the histogram
# has been garbage collected!
canvas.Draw()
# hack to keep Python from exiting
# while the canvas is displayed
raw_input()
