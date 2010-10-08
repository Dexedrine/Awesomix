from pymt import *

class MTQuarter(MTWidget):
    def __init__(self, **kwargs):
        super(MTQuarter, self).__init__(**kwargs)
        self.inner_radius = kwargs.get('inner_radius', 50)
        self.outer_radius = kwargs.get('outer_radius', 100)
        self.start_angle = kwargs.get('start_angle', 0)
        self.end_angle = kwargs.get('end_angle', 360 / 10)

        self.color = kwargs.get('color', (0, 1, 0))
        self.bg_color = kwargs.get('bg_color', (1, 0, 0))
        self._active = False
        #self.min = kwargs.get('min', 0)
        #self.max = kwargs.get('max', 100)

    def draw(self):
        if self._active:
            set_color(*self.bg_color)
        else:
            set_color(*self.color)
        drawSemiCircle(pos=self.pos,
                inner_radius=self.inner_radius,
                outer_radius=self.outer_radius,
                start_angle=self.start_angle,
                sweep_angle=self.end_angle)


if __name__ == '__main__':
    w = getWindow()
    quarter = MTQuarter(pos=w.center)
    runTouchApp(quarter)
