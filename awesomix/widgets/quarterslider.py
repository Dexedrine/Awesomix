from pymt import *
from quarter import MTQuarter

class MTQuarterSlider(MTQuarter):
    def __init__(self, **kwargs):
        super(MTQuarterSlider, self).__init__(**kwargs)
        self.register_event_type('on_value')
        self.slider_color = kwargs.get('slider_color', (255, 0, 255))
        self._value = 0.5

    def on_value(self, value):
        pass

    def _get_value(self):
        return self._value
    def _set_value(self, x):
        val = boundary(0., 1., x)
        if val == self._value:
            return
        self._value = val
        self.dispatch_event('on_value', val)

    value = property(_get_value, _set_value)

    def draw(self):
        super(MTQuarterSlider, self).draw()
        set_color(*self.slider_color)
        drawSemiCircle(pos=self.pos,
                inner_radius=self.inner_radius,
                outer_radius=self.inner_radius + self.value*(self.outer_radius - self.inner_radius),
                start_angle=self.start_angle,
                sweep_angle=self.end_angle)

    def update_widget(self, x, y):
        d = Vector(self.pos).distance((x, y))
        d = boundary(self.inner_radius, self.outer_radius, d) - self.inner_radius
        self.value = d / (self.outer_radius - self.inner_radius)


if __name__ == '__main__':
    w = getWindow()
    '''
    def on_slide_value(index, slide, value):
        print 'mon slider a change la valeur a', index, slide, value
    for x in xrange(3):
        slide = MTQuarterSlider(pos=(100 + x * 100, w.center[1]), id='slide%d' % x)
        slide.connect('on_value', curry(on_slide_value, x, slide))
        w.add_widget(slide)
    '''
    qslider = MTQuarterSlider(pos=w.center)
    pslider = MTSlider(min=0., max=1.)
    qslider.connect('on_value', pslider, 'value')
    pslider.connect('on_value_change', qslider, 'value')
    w.add_widget(qslider)
    w.add_widget(pslider)

    runTouchApp()
