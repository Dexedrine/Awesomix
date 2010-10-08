from pymt import *
from quarter import MTQuarter

class MTQuarterSlider(MTQuarter):
    def __init__(self, **kwargs):
        super(MTQuarterSlider, self).__init__(**kwargs)
        self.slider_radius = kwargs.get('slider_radius', self.inner_radius + 10)
        self.slider_color = kwargs.get('slider_color', (255, 0, 255))
        

    def draw(self):
        super(MTQuarterSlider, self).draw()
        set_color(*self.slider_color)
        drawSemiCircle(pos=self.pos,
                inner_radius=self.inner_radius,
                outer_radius=self.slider_radius,
                start_angle=self.start_angle,
                sweep_angle=self.end_angle)

    def update_slider(self, x, y):
        d = Vector(self.pos).distance((x, y))
        print d
        if d < self.inner_radius :
            self.slider_radius = self.inner_radius
            return
        if d > self.outer_radius:
            self.slider_radius = self.outer_radius
            return


    def on_touch_down(self, touch):
        if super(MTQuarterSlider,self).on_touch_down(touch):
            return True
        print 'on_touch_down()', touch.pos
        if not self.collide_point(*touch.pos):
            return
        self.update_slider(touch.x, touch.y)
        return True

    def on_touch_move(self, touch):
        if super(MTQuarterSlider,self).on_touch_move(touch):
            return True
        print 'on_touch_move()', touch.pos
        if not self.collide_point(*touch.pos):
            return
        self.update_slider(touch.x, touch.y)
        return True


if __name__ == '__main__':
    w = getWindow()
    slide = MTQuarterSlider(pos=w.center)
    slide.add_widget(MTButton())
    runTouchApp(slide)

