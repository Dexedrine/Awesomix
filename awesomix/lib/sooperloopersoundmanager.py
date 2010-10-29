from soundmanager import SoundManager
from simpleOSC import *

class SooperlooperSoundManager(SoundManager):
    def __init__(self, **kwargs):
        super(SooperlooperSoundManager, self).__init__(**kwargs)
        self.addr = kwargs.get('addr','osc.udp://127.0.0.1:9952')
        initOSCServer(port=9952)
        initOSCClient(port=9951)

    def create(self, filename):
        sendOSCMsg('/sl/0/load_loop', [filename, self.addr, '/loop/0'])
        sendOSCMsg('/loop_add', [2, 60])

    def play(self):
        sendOSCMsg('/sl/0/hit',['trigger'])

    def pause(self):
        sendOSCMsg('/sl/0/hit',['pause'])

    def stop(self):
        sendOSCMsg('/loop_del', 0)

