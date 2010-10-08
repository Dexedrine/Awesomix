from pymt import *
from movablecirclewidget import MTMovableCircleWidget

class MTOptionWidget(MTMovableCircleWidget):
    def __init__(self, **kwargs):
        super(MTOptionWidget, self).__init__(**kwargs)

    def on_update(self):
        super(MTOptionWidget, self).on_update()
        angle = 0
        totalzoom = sum([x.lzoom for x in self.children])
        anglestep = 360. / totalzoom
        for index,child in enumerate(self.children):
            child.pos = self.pos
            child.inner_radius = self.radius
            child.start_angle = angle
            child.end_angle = angle + anglestep * child.lzoom
            angle += anglestep * child.lzoom


if __name__ == '__main__':
    win = getWindow()
    circle = MTOptionWidget(pos=win.center)
    for x in xrange(10):
        circle.add_widget(MTButton(label=str(x)))
    runTouchApp(circle)
