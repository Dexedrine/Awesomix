from pymt import *
from quarter import MTQuarter

class MTQuarterSlider(MTQuarter):
    def __init__(self, **kwargs):
        super(MTQuarterSlider, self).__init__(**kwargs)
        self.slider_radius = kwargs.get('slider_radius', 10)
        self.slider_color = kwargs.get('slider_color', (255, 0, 255))
        

    def draw(self):
        super(MTQuarterSlider, self).draw()
        set_color(*self.slider_color)
        drawSemiCircle(pos=self.pos,
                inner_radius=self.inner_radius,
                outer_radius=self.slider_radius+self.inner_radius,
                start_angle=self.start_angle,
                sweep_angle=self.end_angle)



if __name__ == '__main__':
    w = getWindow()
    slide = MTQuarterSlider(pos=w.center)
    runTouchApp(slide)

