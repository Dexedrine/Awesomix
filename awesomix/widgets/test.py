from pymt import *
from optionwidget import MTOptionWidget
from quarterslider import MTQuarterSlider

if __name__ == '__main__':
    win = getWindow()
    circle = MTOptionWidget(pos=win.center)
    for x in xrange(10):
        slider = MTQuarterSlider()
        circle.add_widget(slider)
    runTouchApp(circle)
