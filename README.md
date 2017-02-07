# IFTTT-SmartMirror-WebServer
A simple python webserver for use with my Smart Mirror and IFTTT commands over the internet

## Install Dependencies
Run `sudo apt-get install cec-utils` to handle turning on and off the mirror
Run `sudo apt-get install python3-flask`

## Run server
Run `python3 app.py`

## IFTTT Applets
In order to use IFTTT with the Raspberry Pi, you need to [enable the Maker channel](https://ifttt.com/maker)
- Create a few applets on IFTTT. What I did was have Google Assistant as a trigger and then Maker as the action.
- For Maker,  the URL should be the public IP address of the Pi. `http://PUBLIC_IP:5000/IFTTT`
- Method should be `POST`
- Content type is `application/json`
- Body will be `{ "data": "turn on" }` for turning on the mirror and `{ "data": "turn off" }` for turning it off
