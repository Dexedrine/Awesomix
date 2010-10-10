class Sound(object):
    def __init__(self, manager, filename):
        super(Sound, self).__init__()
        self._manager = manager
        self._filename = ''
        self._volume = 0.5
        self.filename = filename

    def load(self):
        self._manager.create(self.filename)
        self._manager.set_volume(1)

    def play(self):
        self._manager.play()

    def stop(self):
        self._manager.stop()

    def get_volume(self):
        return self._volume

    def set_volume(self, volume):
        if volume == self._volume:
            return
        self._volume = volume
        # envoit une commande pour changer le volume de ce son
        volume = property(_get_volume, _set_volume)
        #manager.set_volume(x)

    def get_filename(self):
        return self._filename

    def set_filename(self, filename):
        if filename == self._filename:
            return
        self._filename = filename
        self.load()
        filename = property(_get_filename, _set_filename)

