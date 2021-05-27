import hub

import utime

import math

 

light = hub.port.F.device

kd = 0.1

kp = 0.3

motorF= hub.port.A.motor

motorE=hub.port.B.motor

motorspin=hub.port.C.motor

speed=35

tape=30

floor=99

Perror = 0

setPoint = (tape+floor)/2

pi = hub.port.A

pi.mode(hub.port.MODE_FULL_DUPLEX)

pi.baud(115200)


 

motorspin.pwm(-45)

while True:

    reply_bytes = pi.read(15)

    utime.sleep(0.1)

    try:

        if reply_bytes:

            reply = reply_bytes.decode('utf-8')

            utime.sleep(0.01)

            resp = str(reply)

            if resp == "on":

                motorspin.pwm(-45)

                speed=35

                try:

                    pos = light.get()[0]

                    error = setPoint - pos

                    derr = error - Perror

                    correction = kp*error + kd*derr

                    motorF.pwm(math.floor(-speed-correction))

                    motorE.pwm(math.floor(speed-correction))

                    utime.sleep(0.005)

                except:

                    utime.sleep(0.005)

            if resp == "off":

                motorspin.pwm(0)

                speed=0

                motorF.pwm(speed)

                motorE.pwm(speed)

    except:

        continue
