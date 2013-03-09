from rootpy.plotting import Canvas, Hist
from rootpy.interactive import wait

def make_plot():
    canvas = Canvas(700, 500)
    hist = Hist(10, -3, 3)
    hist.FillRandom('gaus')
    hist.Draw()
    return canvas

canvas = make_plot()
canvas.Draw()
wait()
