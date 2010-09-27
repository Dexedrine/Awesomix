from pymt import *
from optionwidget import MTOptionWidget
from quarterslider import MTQuarterSlider

if __name__ == '__main__':
    win = getWindow()
    circle = MTOptionWidget(pos=win.center)
    for x in xrange(10):
	slider = MTQuarterSlider(color=(0,0,x))
    	circle.add_widget(slider)
    print(x)
    win.add_widget(circle)
    circle2 = MTOptionWidget(pos=(100, 100))
    circle2.add_widget(MTQuarterSlider())
    win.add_widget(circle2)
    runTouchApp()
