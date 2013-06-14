from django.shortcuts import render_to_response
from django.http import HttpResponse
import json
import serial
TTY_PORT = '/dev/ttyUSB0'
BAUD = 9600

serial_port = serial.Serial(TTY_PORT, BAUD, timeout=1)

def testdj(request):
     a = request.get('ledred','0', type=int)
     if a == 1:
          serial_port.write(chr(0x01))
     elif a == 0:
          serial_port.write(chr(0x11))
     b = request.GET('ledwhite','0',type=int)
          if b == 1:
              serial_port.write(chr(0x03))
          elif b == 0:
              serial_port.write(chr(0x1B))
     c = request.GET('ledyellow','0',type=int)
        if c == 1:
             serial_port.write(chr(0x04))
        elif c == 0:
             serial_port.write(chr(0x1C))
     d = request.GET('ledgreen','0', type=int)
        if d == 1:
             serial_port.write(chr(0x02))
        elif d == 0:
             serial_port.write(chr(0x1A))
     return render_to_response('test.html')

def avr_value(request):
        adc = request.GET('ADC_COMMAND','1', type=int)
        if adc== 1:
            serial_port.write(chr(0x1D))   
            response = serial_port.read(255)
            new = ([("%d" % ord(char)) for char in response])
            one = new[0]
            volt = {'key':one}          
            return jsonify(volt)
        return HttpResponse(0)
