from sound import Sound
from soundmanager import SoundManager
from pygamesoundmanager import PygameSoundManager
from time import sleep

if __name__ == '__main__':
    pygame = PygameSoundManager()
    sound = Sound(pygame, '/home/nico/toto.mp3')
    sound.load()
    sound.play()
    sleep(10)
