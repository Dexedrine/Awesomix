from sound import Sound
from soundmanager import SoundManager
from pygamesoundmanager import PygameSoundManager
from time import sleep
import sys

if __name__ == '__main__':
    pygame = PygameSoundManager()
    sound = Sound(pygame, sys.argv[1], volume=1.)
    sound.load()
    sound.play()
    sleep(10)
    print(sound.get_volume())
