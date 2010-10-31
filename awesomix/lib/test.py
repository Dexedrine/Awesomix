from sound import Sound
from soundmanager import SoundManager
from sooperloopersoundmanager import SooperlooperSoundManager
from pyjack import Pyjack
import sys , time

if __name__ == '__main__':
    pyjack = Pyjack()
    pyjack.connect()
    manager = SooperlooperSoundManager()
    sound = Sound(manager, sys.argv[1])
    sound.load()
    sound.play()
    time.sleep(20)
    sound.pause()
