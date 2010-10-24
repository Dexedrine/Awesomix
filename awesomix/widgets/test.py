from pymt import *
from optionwidget import MTOptionWidget
from quarter import MTQuarter
from quarterbutton import MTQuarterButton
from quarterslider import MTQuarterSlider

if __name__ == '__main__':
    win = getWindow()

    circle = MTOptionWidget(pos=(win.width / 2 + 150, win.height / 2))
    for x in xrange(10):
        slider = MTQuarterButton(color=(x / 20.,0,x / 10.))
        circle.add_widget(slider)
    win.add_widget(circle)

    circle2 = MTOptionWidget(pos=(win.width / 2 - 150, win.height / 2))
    circle2.add_widget(MTQuarterSlider(color=(0.2,0.5,0)))
    circle2.add_widget(MTQuarterSlider(color=(0.5,1,0.5)))
    circle2.add_widget(MTQuarterSlider(color=(0.1,0.1,0.5)))
    button = MTQuarterButton(color=(0,0.2,0.8))
    button2 = MTQuarterButton(color=(1,0.5,0.5))
    circle2.add_widget(button)
    circle2.add_widget(button2)
    win.add_widget(circle2)

    @button2.event
    def on_press(*largs):
        print('on press')

    runTouchApp()
