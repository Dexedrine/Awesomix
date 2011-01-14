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

    #selectEffect = MTOptionWidget(label = 'Effect', label_visible = True, pos = (100, 100))
    #win.add_widget(selectEffect)

    def rate_change(filename, value):
        manager.search(filename).do_rate(value)

    def volume_change(filename, value):
        manager.search(filename).set_volume(value)

    def scratch_change(filename, value):
        manager.search(filename).do_scratch_pos(value)
    
    def reverse_change(filename, self):
        manager.search(filename).do_reverse()

    def ajout(circle, filename):
        y = 1
        rate = MTQuarterSlider(label = 'rate', label_visible = True, color=(y / 50., y / 20., y / 10.), slider_color=(y / 10., 0., y / 10))
        rate.connect('on_value', curry(rate_change, filename))
        circle.add_widget(rate)
        y+=1
        volume = MTQuarterSlider(label = 'volume', label_visible = True, color=(y / 50., y / 20., y / 10.), slider_color=(y / 10., 0., y / 10))
        volume.connect('on_value', curry(volume_change, filename))
        circle.add_widget(volume)
        y+=1
        scratch = MTQuarterSlider(label = 'scratch', label_visible = True, color=(y / 50., y / 20., y / 10.), slider_color=(y / 10., 0., y / 10))
        scratch.connect('on_value', curry(scratch_change, filename))
        circle.add_widget(scratch)
        y+=1
        reverse = MTQuarterButton(label = 'reverse', label_visible = True, color=(y / 50., y / 20., y / 10.), slider_color=(y / 10., 0., y / 10))
        reverse.connect('on_press', curry(reverse_change, filename))
        circle.add_widget(reverse)

    def on_circle_press(filename, *largs):
        manager.search(filename).play()

    def on_button_press(filename, *largs):
        manager.create(filename)
        soundCircle = MTOptionWidget(label=filename)
        win.add_widget(soundCircle)
        soundCircle.connect('on_press', curry(on_circle_press, filename))
        ajout(soundCircle, filename)

    x = 0
    for filename in glob(join(sys.argv[len(sys.argv) - 1], '*.wav')):
        option = MTQuarterButton(label=filename, color=(x / 20.,0,x / 10.))
        selectSound.add_widget(option)
        option.connect('on_press', curry(on_button_press, option.get_label()))
        x+=1

    runTouchApp()
    sendOSCMsg('/quit')
    closeOSC()
