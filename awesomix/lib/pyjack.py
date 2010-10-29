from jack import connect, activate
class Pyjack(object):
    def __init__(self):
        super(Pyjack, self).__init__()

    def connect(self):
        activate()
        connect("sooperlooper:common_out_1", "alsa_pcm:playback_1")
        connect("sooperlooper:common_out_2", "alsa_pcm:playback_2")
