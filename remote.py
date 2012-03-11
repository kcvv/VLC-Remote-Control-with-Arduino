
''' Original Code by Tetzcatlipoca . Modified by Venkatesh 26 Aug 2011
Monitors serial port activity from Arduino on COM2 and sends VLC Http control based on button press
'''

import serial
import urllib2
from time import sleep

# open serial connection

connected = False

try:
    conn = serial.Serial('COM2', 9600);
    sleep(5)
    connected = True
    print "Connected!"
except:
    print "Could not connect to serial port."

while connected:

    inputValue = (conn.readline()[:-2])

    if inputValue == 'FFFFFFFF':
        pass
    elif inputValue ==  '803F3BC4': # Power Button 
        cltrHandle = urllib2.urlopen('http://127.0.0.1:8080/requests/status.xml?command=pl_stop')
        cltrHandle.close()
    elif inputValue == '803F39C6': # Mute Button
        cltrHandle = urllib2.urlopen('http://127.0.0.1:8080/requests/status.xml?command=volume&val=0')
        cltrHandle.close()
    elif inputValue == '803F49B6':
        print "1"
    elif inputValue == '803FC936':
        print "2"
    elif inputValue == '803F33CC':
        print "3"
    elif inputValue == '803F718E':
        print "4"
    elif inputValue == '803FF10E':
        print "5"
    elif inputValue == '803F13EC':
        print "6"
    elif inputValue == '803F51AE':
        print "7"
    elif inputValue == '803FD12E':
        print "8"
    elif inputValue == '803F23DC':
        print "9"
    elif inputValue == '803FA15E':
        print "Help"
    elif inputValue == '803FE11E':
        print "0"
    elif inputValue == '803F817E': # Radio Remapped to Play
        cltrHandle = urllib2.urlopen('http://127.0.0.1:8080/requests/status.xml?command=pl_play')
        cltrHandle.close()
    elif inputValue == '803FBB44':  # Volume Up
        cltrHandle = urllib2.urlopen('http://127.0.0.1:8080/requests/status.xml?command=volume&val=%2B20')
        cltrHandle.close()
    elif inputValue == '803F41BE':
        print "Info"
    elif inputValue == '803F43BC':
        print "Back"
    elif inputValue == '803F19E6': #Channel Up 
        cltrHandle = urllib2.urlopen('http://127.0.0.1:8080/requests/status.xml?command=pl_next')
        cltrHandle.close()
    elif inputValue == '803F31CE': # Volume Down
        cltrHandle = urllib2.urlopen('http://127.0.0.1:8080/requests/status.xml?command=volume&val=-20')
        cltrHandle.close()
    elif inputValue == '803FE916': #Channel Down
        cltrHandle = urllib2.urlopen('http://127.0.0.1:8080/requests/status.xml?command=pl_previous')
        cltrHandle.close()
    elif inputValue == '803F53AC': #Up Key
        cltrHandle = urllib2.urlopen('http://127.0.0.1:8080/requests/status.xml?command=seek&val=+10%')
        cltrHandle.close()
    elif inputValue == '803F9966': #Left Key
        cltrHandle = urllib2.urlopen('http://127.0.0.1:8080/requests/status.xml?command=seek&val=-2%')
        cltrHandle.close()
    elif inputValue == '803F738C':
        cltrHandle = urllib2.urlopen('http://127.0.0.1:8080/requests/status.xml?command=pl_pause')
        cltrHandle.close()
    elif inputValue == '803F837C':  #Right Key 
        cltrHandle = urllib2.urlopen('http://127.0.0.1:8080/requests/status.xml?command=seek&val=+2%')
        cltrHandle.close()
    elif inputValue == '803F4BB4': #Down Key
        cltrHandle = urllib2.urlopen('http://127.0.0.1:8080/requests/status.xml?command=seek&val=-10%')
        cltrHandle.close()
    elif inputValue == '803F11EE':
        print "Menu"
    elif inputValue == '803F619E':
        print "EPG"
    elif inputValue == '803F59A6':
        print "Games"
    elif inputValue == '803FD926':
        print "Interactive"
    elif inputValue == '803FB946':
        print "Language"
    elif inputValue == '803F7986':
        print "Messages"
    elif inputValue == '803FC13E':
        print "Red"
    elif inputValue == '803F5BA4':
        print "Green"
    elif inputValue == '803FB34C':
        print "Yellow"
    elif inputValue == '803F03FC':
        print "Blue"
    elif inputValue == '803FC33C':
        print "Account"
    elif inputValue == '803F936C':
        print "Promo"
    elif inputValue == '803FA35C':
        print "Favorites"
    elif inputValue == '803F639C': #Blank key used for full screen
        cltrHandle = urllib2.urlopen('http://127.0.0.1:8080/requests/status.xml?command=fullscreen')
        cltrHandle.close()
    else :
        print  str(inputValue ) 
   

    sleep(.1)
connected = False
