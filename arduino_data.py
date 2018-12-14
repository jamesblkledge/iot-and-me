# Written By James Blackledge

with open('./arduino.log', 'r') as arduino:
    data = arduino.readlines()[0][-1]
with open('./arduino.txt', 'w') as arduino_responses:
    arduino_responses.write(data)