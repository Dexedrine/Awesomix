from pymt import *
from widgets.movablecirclewidget import MTMovableCircleWidget

from lib.sound import Sound
from lib.soundmanager import SoundManager
from lib.sooperloopersoundmanager import SooperlooperSoundManager
from lib.pyjack import Pyjack

from simpleOSC import *
import sys


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage: python start.py <directory>'
        sys.exit(1)

    win = getWindow()
    pyjack = Pyjack()
    pyjack.connect()
    manager = SooperlooperSoundManager()
    print(sys.argv[1])
    sound = Sound(manager, sys.argv[1])
    sound.load()

    circle = MTMovableCircleWidget(pos=win.center)
    win.add_widget(circle)

    sound.play()
    
    @circle.event
    def on_press(*largs):
        #print(circle.active())
        sound.pause()

    runTouchApp()
    sound.stop()

    sendOSCMsg('/quit')
    closeOSC()
