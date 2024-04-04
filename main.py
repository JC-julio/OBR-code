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
motorSensor = Motor(
    Port.D, positive_direction=Direction.CLOCKWISE, gears=None)
# inicia DriveBase
robo = DriveBase(motorEsquerdo, motorDireito,
                 wheel_diameter=41.9, axle_track=245.9)
# iniciando sensores de cor
CorEsquerda = ColorSensor(Port.S4)
CorDireita = ColorSensor(Port.S1)
ultrassonico = UltrasonicSensor(Port.S3)
# corFrente = ColorSensor(Port.S2)
#posições da garra a partir de sua abertura padrão
fechada = 270
velocidade = 95
abrida = -15
mantemLoop = True

while mantemLoop:
    # motorSensor.run_target(45, fechada, then=Stop.HOLD, wait=True)
    if (ultrassonico.distance() < 50):
        ev3.speaker.beep()
        print(ultrassonico.distance())
    wait(40)
















    # if (ultrassonico.distance() < 50):
    #     print(ultrassonico.distance())
    # #     print(corFrente.color())

    # # robo.drive(90, 0)mio
    # # if (ultrassonico.distance() < 90):
    # #     ev3.speaker.beep()
    # #     robo.turn(180)
    # #     robo.straight(-40)
    # #     motorGarra.run_target(velocidade, fechada, then=Stop.HOLD, wait=True)
    # #     ev3.speaker.beep()
    # #     wait(500)
    # #     mantemLoop = False
    # # print("sensor esquerdo: ",  corFrente.color())
    # # print("sensor direito: ", CorDireita.color())