from sound import Sound
from soundmanager import SoundManager
from soundosc import SoundOsc
from simpleOSC import *

class SooperlooperSoundManager(SoundManager):
    def __init__(self, **kwargs):
        super(SooperlooperSoundManager, self).__init__(**kwargs)
        self.addr = 'osc.udp://127.0.0.1:9951/'
        initOSCServer(port=9952)
        initOSCClient(port=9951)
        self._nextid = 0
        self._sounds = {}
    
    def get_sounds(self):
        return self._sounds

    def nextid(self):
        soundid = self._nextid
        self._nextid += 1
        return soundid


    def create(self, filename):
        soundid = self.nextid()
        sendOSCMsg('/loop_add', [2, 60])
        sound = Sound(self, filename, soundid)
        self._sounds[soundid] = sound
        sendOSCMsg('/sl/%d/load_loop' % soundid, [filename, self.addr, '/loop/%d' % soundid])
        return sound

    def load(self, soundid):
        pass

    def play(self, soundid):
        sendOSCMsg('/sl/%d/hit' %soundid, ['trigger'])

    def pause(self, soundid):
        sendOSCMsg('/sl/%d/hit' %soundid, ['pause'])

    def stop(self, soundid):
        sendOSCMsg('/loop_del', ['%d'] %soundid)

    #Retourne le son du filename
    def search(self, filename):
        for index in self._sounds:
            if self._sounds[index].get_filename() == filename:
                return self._sounds[index]

    def set_volume(self, soundid, volume):
        sendOSCMsg('/sl/%d/set' %soundid, ['wet', volume])

    def do_rate(self, soundid, value):
        sendOSCMsg('/sl/%d/set' %soundid, ['rate', int(value * 5)])

    def do_scratch_pos(self, soundid, value):
        sendOSCMsg('/sl/%d/set' %soundid, ['scratch_pos', value])
