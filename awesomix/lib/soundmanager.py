class SoundManager(object):
    def __init__(self, **kwargs):
        super(SoundManager, self).__init__(**kwargs)

    def set_volume(self, soundid, volume):
        pass
    
    def create(self, filename):
        pass
    
    def load(self, soundid):
        pass

    def play(self, soundid):
        pass

    def pause(self, soundid):
        pass

    def stop(self, soundid):
        pass
    
    def search(self, filename):
        pass

    def do_rate(self, soundid, value):
        pass

    def do_scratch_pos(self, soundid, value):
        pass
