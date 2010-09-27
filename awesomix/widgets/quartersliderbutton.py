from pymt import *
from quarterslider import MTQuarterSlider
from math import cos, sin, pi

class MTQuarterSliderButton(MTQuarterSlider):
    def __init__(self, **kwargs):
        super(MTQuarterSliderButton, self).__init__(**kwargs)
        self._active = False
        self._active_touch = None

    def collide_point(self, x, y):
        curpos = Vector(self.pos)
        touchpos = Vector(x, y)
        distance = curpos.distance(touchpos)
        a = Vector(self.x + (self.inner_radius * sin(2 * pi * self.start_angle / 360)),
                self.y +(self.inner_radius * cos(2 * pi * self.start_angle / 360)))
        b = Vector(self.x + (self.inner_radius * sin(2 * pi * self.start_angle + self.end_angle / 360)),
                self.y +(self.inner_radius * cos(2 * pi * self.start_angle + self.end_angle/ 360)))
        c = Vector(self.x + (self.outer_radius * sin(2 * pi * self.start_angle / 360)),
                self.y +(self.outer_radius * cos(2 * pi * self.start_angle / 360)))
        d = Vector(self.x + (self.outer_radius * sin(2 * pi * self.start_angle + self.end_angle / 360)),
                self.y +(self.outer_radius * cos(2 * pi * self.start_angle + self.end_angle/ 360)))
        #i = line_intersection(a, b, c, d)
        #distance2 = i.distance(touchpos)
        print(distance)
        if ((distance >= self.inner_radius) and (distance <= self.outer_radius)):
            return True
        else:
            return False


    def on_touch_down(self, touch):
        if self._active:
            return super(MTQuarterSliderButton, self).on_touch_down(touch)
        if not self.collide_point(touch.x, touch.y):
            return
        self._active = True
        self._active_touch = touch.uid
        print('Touch')
        return True

    def on_touch_up(self, touch):
        if touch.uid != self._active_touch:
            return
        self._active = False
        return True

#    def draw(self):
        #if self._active:
            #set_color(0, 1, 0)
        #else:
            #set_color(0, 0, 1)
        #super(MTQuarterSlider, self).draw()

if __name__ == '__main__':
    w = getWindow()
    slider = MTQuarterSliderButton(pos=w.center)
    runTouchApp(slider)
