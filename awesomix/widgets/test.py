from pymt import *
from optionwidget import MTOptionWidget
from quarterslider import MTQuarterSlider
from quartersliderbutton import MTQuarterSliderButton

if __name__ == '__main__':
    win = getWindow()
    circle = MTOptionWidget(pos=win.center)
    for x in xrange(10):
        slider = MTQuarterSliderButton(color=(20*x,0,10*x))
        circle.add_widget(slider)
    win.add_widget(circle)
    circle2 = MTOptionWidget(pos=(100, 100))
    circle2.add_widget(MTQuarterSliderButton(color=(1,0,0)))
    win.add_widget(circle2)
    runTouchApp()
