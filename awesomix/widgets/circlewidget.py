from pymt import *

class MTCircleWidget(MTWidget):
    def __init__(self, **kwargs):
        super(MTCircleWidget, self).__init__(**kwargs)
        self.radius = kwargs.get('radius', 50)
        self.color = kwargs.get('color', (0.5, 0, 0.8))
        self.bg_color = kwargs.get('bg_color', (0.8, 0, 0.5))
        self._active = False
        self._active_touch = None

        self.register_event_type('on_press')
        self.register_event_type('on_release')

    def on_press(self, *largs):
        pass

    def on_release(self, *largs):
        pass

    def collide_point(self, x, y):
        curpos = Vector(self.pos)
        touchpos = Vector(x, y)
        distance = curpos.distance(touchpos)
        return distance <= self.radius

    def on_touch_down(self, touch):
        if self._active:
           return super(MTCircleWidget, self).on_touch_down(touch)
        #if super(MTCircleWidget, self).on_touch_down(touch):
            #return True
        if not self.collide_point(touch.x, touch.y):
            return
        self._active = True
        self._active_touch = touch.uid
        self.dispatch_event('on_press', touch)
        return True

    def on_touch_up(self, touch):
        if super(MTCircleWidget, self).on_touch_up(touch):
            return True
        if touch.uid != self._active_touch:
            return
        self._active = False
        self.dispatch_event('on_release', touch)
        return True

    def draw(self):
        if self._active:
            set_color(*self.bg_color)
        else:
            set_color(*self.color)
        drawCircle(pos=self.pos, radius=self.radius)

    @property
    def active(self):
        return self._active

if __name__ == '__main__':
    win = getWindow()
    for x in xrange(4):
        circle = MTCircleWidget(pos=((win.width / 4.)*x + 50., win.height / 2.))
        win.add_widget(circle)
    
    circle2 = MTCircleWidget(pos=(win.width / 2., 100))
    win.add_widget(circle2)
    @circle2.event
    def on_press(*largs):
        print("on press")

    runTouchApp()
