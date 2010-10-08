from pymt import *
from quarter import MTQuarter
from math import cos, sin, radians

class MTQuarterButton(MTQuarter):
    def __init__(self, **kwargs):
        super(MTQuarterButton, self).__init__(**kwargs)
        self._active_touch = None
        self.rotation = self.start_angle;
        self._radius_line = self.outer_radius * sin(radians(self.rotation)), \
                              self.outer_radius * cos(radians(self.rotation))

    def collide_point(self, x, y):
        cx, cy = self.pos
        point_dist = Vector(self.pos).distance((x, y))
        point_angle = Vector(self._radius_line).angle((x - cx, y - cy))
        if point_angle < 0:
            point_angle = 360. + point_angle
        if 0 < point_angle > self.end_angle:
            return False
        return self.inner_radius < point_dist <= self.outer_radius

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
        print("toto")
        return True

if __name__ == '__main__':
    w = getWindow()
    button = MTQuarterButton(pos=w.center)
    runTouchApp(button)
