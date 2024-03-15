#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor, UltrasonicSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase

ev3 = EV3Brick()
# Create your objects here.#inicando motores
motorEsquerdo = Motor(
    Port.A, positive_direction=Direction.CLOCKWISE, gears=None)
motorDireito = Motor(
    Port.B, positive_direction=Direction.CLOCKWISE, gears=None)
motorGarra = Motor(
    Port.C, positive_direction=Direction.CLOCKWISE, gears=None)
# inicia DriveBase
robo = DriveBase(motorEsquerdo, motorDireito,
                 wheel_diameter=41.9, axle_track=244.3)
# iniciando sensores de cor
CorEsquerda = ColorSensor(Port.S4)
CorDireita = ColorSensor(Port.S1)
ultrassonico = UltrasonicSensor(Port.S3)

fechada = 270
velocidade = 95
abrida = -15,

motorGarra.run_target(velocidade, fechada, then=Stop.HOLD, wait=True)
ev3.speaker.beep()
wait(500)
motorGarra.run_target(velocidade, abrida, then=Stop.HOLD, wait=True)
wait(500)
ev3.speaker.beep()
motorGarra.run_target(velocidade, fechada, then=Stop.HOLD, wait=True)
ev3.speaker.beep()
wait(500)
motorGarra.run_target(velocidade, abrida, then=Stop.HOLD, wait=True)
ev3.speaker.beep()
wait(500)
