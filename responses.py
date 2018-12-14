# Written By James Blackledge

with open('alexa.txt', 'r') as alexa:
    alexa_data = alexa.readlines()[0]
    
with open('spotify.txt', 'r') as spotify:
    spotify_data = spotify.readlines()[0]

with open('hue.txt', 'r') as hue:
    hue_data = hue.readlines()[0]

with open('arduino.txt', 'r') as arduino:
    arduino_data = arduino.readlines()[0]

with open('responses.txt', 'w') as responses:
    responses.write("Alexa, Sonos, Phue, Arduino\n{}, {}, {}, {}".format(alexa_data, spotify_data, hue_data, arduino_data))