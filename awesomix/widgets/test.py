from pymt import *
from optionwidget import MTOptionWidget
from quarter import MTQuarter
from quarterbutton import MTQuarterButton

if __name__ == '__main__':
    win = getWindow()
    circle = MTOptionWidget(pos=win.center)
    for x in xrange(10):
        slider = MTQuarterButton(color=(x / 20.,0,x / 10.))
        circle.add_widget(slider)
    win.add_widget(circle)
    circle2 = MTOptionWidget(pos=(100, 100))
    circle2.add_widget(MTQuarterSliderButton(color=(1,0,0)))
    circle2.add_widget(MTQuarterSliderButton(color=(0,1,0)))
    win.add_widget(circle2)
    runTouchApp()
