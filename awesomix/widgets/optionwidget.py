from pymt import *
from movablecirclewidget import MTMovableCircleWidget
from math import cos, sin, pi

class MTOptionWidget(MTMovableCircleWidget):
    def on_update(self):
        super(MTOptionWidget, self).on_update()
        print self.children
        angle = 0
        r = self.radius + 50
        for index,child in enumerate(self.children):
            child.center = (
                    (self.x + r * sin(angle)),
                    (self.y + r * cos(angle)))
            angle += 2* pi / len(self.children)



if __name__ == '__main__':
    win = getWindow()
    circle = MTOptionWidget(pos=win.center)
    for x in xrange(10):
        circle.add_widget(MTButton(label=str(x)))
    runTouchApp(circle)
