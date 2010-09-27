from pymt import *
from math import fabs

class MTQuarterSlider(MTWidget):
    def __init__(self, **kwargs):
        super(MTQuarterSlider, self).__init__(**kwargs)
        #self.min = kwargs.get('min', 0)
        #self.max = kwargs.get('max', 100)
        self.inner_radius = kwargs.get('inner_radius', 50)
        self.outer_radius = kwargs.get('outer_radius', 100)
        self.start_angle = kwargs.get('start_angle', 0)
        self.end_angle = kwargs.get('end_angle', 360 / 10)


    def draw(self):
        set_color(1,0,0) 
        sweep_angle = fabs(self.end_angle - self.start_angle)
        drawSemiCircle(pos=self.pos, inner_radius=self.inner_radius, outer_radius=self.outer_radius, start_angle=self.start_angle, sweep_angle=sweep_angle)


if __name__ == '__main__':
    w = getWindow()
    slider = MTQuarterSlider(pos=w.center)
    runTouchApp(slider)
