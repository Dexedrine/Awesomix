from pymt import *
from math import pi, fabs

class MTQuarterSlider(MTWidget):
    def __init__(self, **kwargs):
        super(MTQuarterSlider, self).__init__(**kwargs)
        self.min = kwargs.get('min', 0)
        self.max = kwargs.get('max', 100)
        self.radius = kwargs.get('radius', 100)
        self.start_angle = kwargs.get('start_angle', 0)
        self.end_angle = kwargs.get('end_angle', 2 * pi / 10)


    def draw(self):
        super(MTQuarterSlider, self).draw()
        set_color(0,1,0)
        i = self.radius * fabs(self.start_angle - self.end_angle)
        o = (self.radius + 100) * fabs(self.start_angle - self.end_angle)
        sweep_angle = fabs(self.end_angle - self.start_angle)
        print(i,o)
        drawSemiCircle(pos=self.pos, inner_radius=i, outer_radius=o, start_angle=self.start_angle, sweep_angle=sweep_angle)


if __name__ == '__main__':
    w = getWindow()
    slider = MTQuarterSlider(pos=(500, 500))
    runTouchApp(slider)
