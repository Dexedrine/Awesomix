from pymt import *

class MTCircleWidget(MTWidget):
    def __init__(self, **kwargs):
        super(MTCircleWidget, self).__init__(**kwargs)
        self.radius = kwargs.get('radius', 50)
        self.color = kwargs.get('color', (0, 1, 0))
        self.bg_color = kwargs.get('bg_color', (0, 0, 1))
        self._active = False
        self._active_touch = None

    def collide_point(self, x, y):
        curpos = Vector(self.pos)
        touchpos = Vector(x, y)
        distance = curpos.distance(touchpos)
        return distance <= self.radius

    def on_touch_down(self, touch):
        if self._active:
           return super(MTCircleWidget, self).on_touch_down(touch)
        #if super(MTCircleWidget, self).on_touch_down(touch):
            #return True
        if not self.collide_point(touch.x, touch.y):
            return
        self._active = True
        self._active_touch = touch.uid
        return True

    def on_touch_up(self, touch):
        if super(MTCircleWidget, self).on_touch_up(touch):
            return True
        if touch.uid != self._active_touch:
            return
        self._active = False
        return True

    def draw(self):
        if self._active:
            set_color(0, 1, 0)
        else:
            set_color(0, 0, 1)
        drawCircle(pos=self.pos, radius=self.radius)

    @property
    def active(self):
        return self._active
