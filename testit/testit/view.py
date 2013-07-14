from django.template.loader import get_template
from django.http import HttpResponse
from django.template import Template, Context
import serial
import json
TTY_PORT = '/dev/ttyUSB0'
BAUD = 9600
s = serial.Serial(TTY_PORT, BAUD, timeout=1)
red = 0
green = 0
yellow = 0
adc = 0
def main(request):
    global adc
    global red
    global green
    global yellow
    t = get_template('new.html')
    out = t.render(Context({}))
    if request.method == 'GET':
        a = request.GET.get('red', red)
        if a != red:
            red = a
            if red == '1':
                s.write(chr(0x01))
            elif red == '0':
                s.write(chr(0x11))
	b = request.GET.get('green', green)
        if b != green:
            green = b
            if green == '1':
                s.write(chr(0x03))
            elif green == '0':
                s.write(chr(0x1B))
	c = request.GET.get('yelliow',yellow)
        if c != yellow:
            yellow = b
            if yellow == '1':
                s.write(chr(0x02))
            elif yellow == '0':
                s.write(chr(0x1A))
    return HttpResponse(out)

def avr(request):
    global adc
    if request.method == 'GET':
	adc = request.GET.get('adc', adc)
        print adc
        if adc == '1':
              s.write(chr(0x1D))
              out = s.read(255)
    return HttpResponse(out)
