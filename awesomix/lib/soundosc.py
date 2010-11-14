class SoundOsc(object):
    def __init__(self):
        pass

    def send(self, path, params):
        print '/sl/%d/%s' % (self.loopid, path), params
        sendOSCMsg('/sl/%d/%s' % (self.loopid, path), params)

    def receive(self, addr, tags, data, source):
        print 'loop', self.loopid, 'receive: addr=',addr,
        print 'tags=', tags, 'data=', data, 'source=', source
