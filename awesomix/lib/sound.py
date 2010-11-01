class Sound(object):
    def __init__(self, manager, filename, soundid, **kwargs):
        super(Sound, self).__init__(**kwargs)
        self._manager = manager
        self._filename = filename
        self.soundid = soundid
        self._volume = kwargs.get('volume', 0.5)
        self.volume = self._volume
        self._pause = False


    def load(self):
        self._manager.load(self.soundid)

    def play(self):
        self._manager.play(self.soundid)

    def pause(self):
        if (self._pause == False):
            self._manager.pause(self.soundid)
            self._pause = True
        else:
            self._manager.play(self.soundid)
            self._pause = False

    def stop(self):
        self._manager.stop(self.soundid)

    def get_volume(self):
        return self._volume

    def set_volume(self, volume):
        if volume == self._volume:
            return
        self._volume = volume
        # envoit une commande pour changer le volume de ce son
        volume = property(_get_volume, _set_volume)

    def get_filename(self):
        return self._filename

    def set_filename(self, filename):
        if filename == self._filename:
            return
        self._filename = filename
        self.load()
        filename = property(_get_filename, _set_filename)
