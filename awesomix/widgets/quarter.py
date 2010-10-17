from pymt import *
from math import cos, sin, radians

class MTQuarter(MTWidget):
    def __init__(self, **kwargs):
        super(MTQuarter, self).__init__(**kwargs)
        self.zoom = kwargs.get('zoom', 1.)
        self.lzoom = self.zoom
        self.inner_radius = kwargs.get('inner_radius', 50)
        self._outer_radius = kwargs.get('outer_radius', 100)
        self.start_angle = kwargs.get('start_angle', 0)
        self.end_angle = kwargs.get('end_angle', 360 / 10)

        self.color = kwargs.get('color', (255, 165, 0))
        self.bg_color = kwargs.get('bg_color', (250, 250, 250))
        #activation a false par defaut
        self._active = False
        #valeur du zoom par defaut =5
        self.active_zoom = kwargs.get('active_zoom', 5)
        #par defaut none mais prend l'idch du premier doigt, c'est l'uid qui controle les actions
        self._active_touch = None

    @property
    def outer_radius(self):
        return self._outer_radius + ((self.lzoom - 1) * 10)

    def _get_active(self):
        return self._active
    def _set_active(self, x):
        self._active = x
        if self._active == True:
            self.zoom = self.active_zoom
        else:
            self.zoom = 1
    #detecte automatiquement lorsque l'on get ou set !         
    active = property(_get_active, _set_active)

    def update_widget(self, x, y):
        pass

    def collide_point(self, x, y):
        cx, cy = self.pos
        radius_line = self.outer_radius * sin(radians(self.start_angle)), \
                              self.outer_radius * cos(radians(self.start_angle))
        point_dist = Vector(self.pos).distance((x, y))
        point_angle = Vector(radius_line).angle((x - cx, y - cy))
        if point_angle < 0:
            point_angle = 360. + point_angle
        if 0 < point_angle > self.end_angle - self.start_angle:
            return False
        return self.inner_radius < point_dist <= self.outer_radius

    def on_touch_down(self, touch):
        if super(MTQuarter,self).on_touch_down(touch):
            return True
        if not self.collide_point(*touch.pos):
            return
        if self._active_touch is not None:
           return
        self._active_touch = touch.uid
        self.active = True
        self.update_widget(*touch.pos)
        self.dispatch_event('on_release')
        self.dispatch_event('on_state_change', self.active)
        return True


    def on_touch_up(self, touch):
        if touch.uid != self._active_touch:
            return
        if super(MTQuarter,self).on_touch_up(touch):
            return True
        self.active = False
        self._active_touch = None
        self.dispatch_event('on_press')
        self.dispatch_event('on_state_change', self.active)
        return True

    def on_touch_move(self,touch):
        if super(MTQuarter,self).on_touch_move(touch):
            return True
        if not self.collide_point(*touch.pos):
            return
        if touch.uid != self._active_touch:
            return
        self.update_widget(*touch.pos)
        return True

    def draw(self):
        if self._active:
            set_color(*self.bg_color)
        else:
            set_color(*self.color)
        drawSemiCircle(pos=self.pos,
                inner_radius=self.inner_radius,
                outer_radius=self.outer_radius,
                start_angle=self.start_angle,
                sweep_angle=self.end_angle - self.start_angle)

    def on_update(self):
        super(MTQuarter, self).on_update()
        self.lzoom = interpolate(self.lzoom, self.zoom, 5)

    def on_press(self):
        pass

    def on_release(self):
        pass

    def on_state_change(self, state):
        return state

if __name__ == '__main__':
    w = getWindow()

    button = MTButton(label='push me')
    w.add_widget(button)

    quarter = MTQuarter(pos=w.center)
    w.add_widget(quarter)

    def on_button_press(*l):
        quarter.active = not quarter.active
    button.connect('on_press', on_button_press)

    runTouchApp()
