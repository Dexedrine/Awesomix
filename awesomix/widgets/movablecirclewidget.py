from pymt import *
from circlewidget import MTCircleWidget

class MTMovableCircleWidget(MTCircleWidget):
    def on_touch_down(self, touch):
        if not super(MTMovableCircleWidget, self).on_touch_down(touch):
            return
        # calcul dx, dy
        touch.userdata['movable.dx'] = touch.x - self.x
        touch.userdata['movable.dy'] = touch.y - self.y
        return True

    def on_touch_move(self, touch):
        if not self.active:
            return
        if touch.uid != self._active_touch:
            return
        self.x = touch.x - touch.userdata['movable.dx']
        self.y = touch.y - touch.userdata['movable.dy']
        return True

if __name__ == '__main__':
    win = getWindow()
    for x in xrange(5):
        circle = MTMovableCircleWidget(pos=(50 + x * 150, win.height / 2.))
        win.add_widget(circle)
    runTouchApp()
