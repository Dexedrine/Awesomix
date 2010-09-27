from pymt import *
from quarterslider import MTQuarterSlider

class MTQuarterSliderButton(MTQuarterSlider):
    def __init__(self, **kwargs):
        super(MTQuarterSliderButton, self).__init__(**kwargs)
        self._active = False
        self._active_touch = None

    def collide_point(self, x, y):
        curpos = Vector(self.pos)
        touchpos = Vector(x, y)
        distance = curpos.distance(touchpos)
        a = self.inner_radius * self.end_angle
        b = self.outer_radius * self.end_angle
        print(distance, a, b)
        if ((self.inner_radius >= distance) and (distance <= self.outer_radius)):
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
 #       super(MTQuarterSlider, self).draw()

if __name__ == '__main__':
    w = getWindow()
    slider = MTQuarterSliderButton(pos=w.center)
    runTouchApp(slider)
