from pymt import *
from quarterslider import MTQuarterSlider
from math import cos, sin, radians

class MTQuarterSliderButton(MTQuarterSlider):
    def __init__(self, **kwargs):
        super(MTQuarterSliderButton, self).__init__(**kwargs)
        self._active = False
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
            return super(MTQuarterSliderButton, self).on_touch_down(touch)
        if not self.collide_point(touch.x, touch.y):
            return
        self._active = True
        self._active_touch = touch.uid
        self.color = (200,200,200)
        return True

    def on_touch_up(self, touch):
        if touch.uid != self._active_touch:
            return
        self._active = False
        self.color = self._color
        return True

if __name__ == '__main__':
    w = getWindow()
    slider = MTQuarterSliderButton(pos=w.center)
    runTouchApp(slider)
