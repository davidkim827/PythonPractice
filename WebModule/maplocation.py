#!/usr/bin/env python3
# mapit.py - Launches a map in the browser using an address from the
# command line

#example usage: py mapit.py 1600 Pennsylvania Ave NW, Washington, DC 20500

import webbrowser, sys

if len(sys.argv) > 1:
    address = " ".join(sys.argv[1:])
    
webbrowser.open("https://www.google.com/maps/place/" + address)

