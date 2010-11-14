from sound import Sound
from soundmanager import SoundManager
from soundosc import SoundOsc
from simpleOSC import *

class SooperlooperSoundManager(SoundManager):
    def __init__(self, **kwargs):
        super(SooperlooperSoundManager, self).__init__(**kwargs)
        self.addr = kwargs.get('addr','osc.udp://127.0.0.1:9951/')
        initOSCServer(port=9952)
        initOSCClient(port=9951)
        self._nextid = 0
        osc2 = SoundOsc()

    def nextid(self):
        soundid = self._nextid
        self._nextid += 1
        return soundid


    def create(self, filename):
        soundid = self.nextid()
        sendOSCMsg('/sl/%d/load_loop' % soundid, [filename, self.addr, '/loop/%d' % soundid])
        sendOSCMsg('/loop_add', [2, 60])
        sound = Sound(self, filename, soundid)
        #setOSCHandler('/loop/%d' % soundid, osc2.receive())
        return sound

    def load(self, soundid):
        pass

    def play(self, soundid):
        sendOSCMsg('/sl/%d/hit' %soundid, ['trigger'])

    def pause(self, soundid):
        sendOSCMsg('/sl/%d/hit' %soundid,['pause'])

    def stop(self, soundid):
        sendOSCMsg('/loop_del', ['%d'] %soundid)
