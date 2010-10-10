from pymt import *
from quarter import MTQuarter

class MTQuarterButton(MTQuarter):
    def __init__(self, **kwargs):
        super(MTQuarterButton, self).__init__(**kwargs)

if __name__ == '__main__':
    w = getWindow()
    button = MTQuarterButton(pos=w.center)
    button2 = MTQuarterButton(pos=w.center, start_angle=100)
    w.add_widget(button)
    w.add_widget(button2)
    runTouchApp()
