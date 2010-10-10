from soundmanager import SoundManager
import pygame

class PygameSoundManager(SoundManager):
    def __init__(self):
        super(PygameSoundManager, self).__init__()
        pygame.init()
        self.music = pygame.mixer.music

    def create(self, filename):
        self.music.load(filename)

    def play(self):
        self.music.play()

    def stop(self):
        self.music.stop()

    def set_volume(self, volume):
        self.music.set_volume(volume)
