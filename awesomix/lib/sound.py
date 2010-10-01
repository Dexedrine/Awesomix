class Sound(object):
    def __init__(self, manager, filename):
        super(Sound, self).__init__()
        self._manager = manager
        self._filename = ''
        self._volume = 0.5
        self.filename = filename

    def load(self):
        manager.create(self.filename)

    def play(self):
        manager.play()

    def stop(self):
        manager.stop()
