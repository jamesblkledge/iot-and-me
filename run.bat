:: Written By James Blackledge

@ECHO OFF

START /B py "alexa_data.py"
START /B py "spotify_data.py"
:: Follow The Above Line With Your Spotify Username
START /B py "hue_data.py"
START /B py "arduino_data.py"

TIMEOUT 2

START /B py "responses.py"
START /B py "data.py"