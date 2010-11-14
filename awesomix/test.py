from pymt import *
from widgets.movablecirclewidget import MTMovableCircleWidget
from widgets.optionwidget import MTOptionWidget
from widgets.quarterbutton import MTQuarterButton

from lib.sound import Sound
from lib.soundmanager import SoundManager
from lib.sooperloopersoundmanager import SooperlooperSoundManager
from lib.pyjack import Pyjack

from simpleOSC import *
import sys, os
from os.path import realpath, join
from glob import glob

class AudioOption(MTOptionWidget):
    def draw(self):
        super(AudioOption, self).draw()
        drawLabel(self.audio.soundid, pos=self.pos, font_size=24)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage: python start.py <directory>'
        sys.exit(1)

    win = getWindow()
    pyjack = Pyjack()
    pyjack.connect()
    manager = SooperlooperSoundManager()

    for filename in glob(join(sys.argv[1], '*.wav')):
        sound = manager.create(filename)
        sound.play()
        
        option = AudioOption()
        option.audio = sound
        win.add_widget(option)

        @option.event
        def on_press(*largs):
            sound.pause()


    runTouchApp()

    sendOSCMsg('/quit')
    closeOSC()
