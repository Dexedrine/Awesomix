#!/usr/bin/env python
# fichier principal

import subprocess, sys

#Lancement de qjackctl
#qjackctl = subprocess.Popen("qjackctl")
#qjackctl.poll()

#Lancement de sooperlooper
sooperlooper = subprocess.Popen("sooperlooper")
sooperlooper.poll()

awesomix = subprocess.Popen([sys.executable, 'awesomix/test.py'] + sys.argv[1:])
awesomix.wait()
