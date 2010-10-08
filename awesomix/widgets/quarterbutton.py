from pymt import *
from quarter import MTQuarter

class MTQuarterButton(MTQuarter):
    def __init__(self, **kwargs):
        super(MTQuarterButton, self).__init__(**kwargs)
        self._active_touch = None

    def on_touch_down(self, touch):
        if self._active:
            return super(MTQuarterButton, self).on_touch_down(touch)
        if not self.collide_point(touch.x, touch.y):
            return
        self._active = True
        self._active_touch = touch.uid
        return True

    def on_touch_up(self, touch):
        if touch.uid != self._active_touch:
            return
        self._active = False
        return True

if __name__ == '__main__':
    w = getWindow()
    button = MTQuarterButton(pos=w.center)
    button2 = MTQuarterButton(pos=w.center, start_angle=100)
    w.add_widget(button)
    w.add_widget(button2)
    runTouchApp()
