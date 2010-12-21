from pymt import *
from widgets.movablecirclewidget import MTMovableCircleWidget
from widgets.optionwidget import MTOptionWidget
from widgets.quarterbutton import MTQuarterButton
from widgets.quarterslider import MTQuarterSlider

from lib.sound import Sound
from lib.soundmanager import SoundManager
from lib.sooperloopersoundmanager import SooperlooperSoundManager
from lib.pyjack import Pyjack

from simpleOSC import *
import sys, os
from os.path import realpath, join
from glob import glob


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage: python start.py [option] <directory>'
        sys.exit(1)

    win = getWindow()
    pyjack = Pyjack()
    pyjack.connect()
    manager = SooperlooperSoundManager()

    selectSound = MTOptionWidget(label = 'Select', label_visible = True, pos = win.center)
    win.add_widget(selectSound)

    selectEffect = MTOptionWidget(label = 'Effect', label_visible = True, pos = (100, 100))
    win.add_widget(selectEffect)

    def ajout(circle):
        rate = MTQuarterSlider()
        circle.add_widget(rate)

    #Retourne le son du filename
    def search(filename):
        #Recuperation de la liste des sons
        sounds = manager.get_sounds()
        for index in sounds:
            if sounds[index].get_filename() == filename:
                return sounds[index]

    def on_circle_press(filename, *largs):
        search(filename).play()

    def on_button_press(filename, *largs):
        manager.create(filename)
        soundCircle = MTOptionWidget(label=filename)
        win.add_widget(soundCircle)
        soundCircle.connect('on_press', curry(on_circle_press, filename))
        ajout(soundCircle)

    x = 0
    for filename in glob(join(sys.argv[len(sys.argv) - 1], '*.wav')):
        option = MTQuarterButton(label=filename, color=(x / 20.,0,x / 10.))
        selectSound.add_widget(option)
        option.connect('on_press', curry(on_button_press, option.get_label()))
        x+=1

    runTouchApp()
    sendOSCMsg('/quit')
    closeOSC()
