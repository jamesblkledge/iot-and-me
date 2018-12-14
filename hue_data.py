# Written By Sean Stanfield

from phue import Bridge

b = Bridge('192.168.0.100')
b.connect()

colour = 0
colourCode = 0

bri = b.get_light(1, 'bri')
hue = b.get_light(1, 'hue')
sat = b.get_light(1, 'sat')

if hue == 925:
    colour = 'red'
    colourCode = '1'
elif hue == 40686:
    colour = 'blue'
    colourCode = '2'
elif hue == 29618:
    colour = 'green'
    colourCode = '3'
elif hue == 17373:
    colour = 'yellow'
    colourCode = '4'
else:
    colour = 'other'
    colourCode = '0'

with open('./hue.txt', 'w') as hue_responses:
    hue_responses.write(colourCode)
    
print(bri, sat, hue, colour, colourCode)