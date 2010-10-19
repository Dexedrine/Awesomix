from pymt import *
from optionwidget import MTOptionWidget
from quarter import MTQuarter
from quarterbutton import MTQuarterButton
from quarterslider import MTQuarterSlider

if __name__ == '__main__':
    win = getWindow()
    circle = MTOptionWidget(pos=win.center)
    for x in xrange(10):
        slider = MTQuarterButton(color=(x / 20.,0,x / 10.))
        circle.add_widget(slider)
    win.add_widget(circle)
    circle2 = MTOptionWidget(pos=(win.width / 2 - 250, win.height / 2))
    circle2.add_widget(MTQuarterSlider(color=(0,1,0)))
    circle2.add_widget(MTQuarterSlider(color=(0.5,1,0.5)))
    circle2.add_widget(MTQuarterSlider(color=(0.1,0.1,0.5)))
    button = MTQuarterButton(color=(1,0,0))
    button3 = MTQuarterButton(color=(1,0.5,0.5))
    circle2.add_widget(button)
    circle2.add_widget(button3)
    win.add_widget(circle2)

    def on_button_press(index):
        print(index)

    button2 = MTQuarterButton(color=(1,0,0))
    #button2.connect('on_press', curry('on_button_press', 'toto'))
    win.add_widget(button2)
    @button2.event
    def on_state_change(*largs):
        print(toto)

    @button2.event
    def on_press(*largs):
        print(toto)

    runTouchApp()
