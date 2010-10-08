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
        self._active = False

    @property
    def outer_radius(self):
        return self._outer_radius + ((self.lzoom - 1) * 10)

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



if __name__ == '__main__':
    w = getWindow()
    quarter = MTQuarter(pos=w.center)
    runTouchApp(quarter)
