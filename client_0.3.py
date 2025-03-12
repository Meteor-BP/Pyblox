#------------ИМПОРТ БИБЛИОТЕК------------
from ursina import *
from ursina.networking import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random
#import socket
#------------ИМПОРТ БИБЛИОТЕК------------

App = Ursina() # Иницилизируем 3д движок

#------------ПЕРЕМЕННЫЕ------------
fallspeed = 0 # Скорость падения
isGround = 0 # На земле ли мы

#ID = random.randint(0, 100) # Айди игрока

MessagesToSend = [] # Сообщения на отправку

global isFirstCam
isFirstCam = False

cam = FirstPersonController() # Создаем камеру
cam.gravity = 0 # Отключаем физику (сделал свою)

players = []
#------------ПЕРЕМЕННЫЕ------------


#------------Клиентская часть------------

#def listofplayers(pos):
#    global players
#
#    client = socket.socket()            # создаем сокет клиента
#    hostname = socket.gethostname()     # получаем хост локальной машины
#    port = 12345                        # устанавливаем порт сервера
#    client.connect((hostname, port))    # подключаемся к серверу
#    message = str(str(ID) + ", pos: " + str(pos))   # вводим сообщение
#    client.send(message.encode())       # отправляем сообщение серверу
#    data = client.recv(1024)            # получаем данные с сервера
#    str(data)
#    print(" ") # Пустота
#    print(" ") # Пустота
#    print("Актуальный список игроков: ", data.decode())    # выводим данные на консоль
#    client.close()                      # закрываем подключение
#
#print("Мой айди:" + str(ID)) # Мой айди
#print(" ") # Пустота
#print(" ") # Пустота

#------------Клиентская часть------------


#------------СОЗДАНИЕ ИГРОКОВ------------
playerHead = Entity(model="cube", color=color.yellow, scale=0.6, collider='mesh', parent = cam)
playerTorso = Entity(model="cube", color=color.blue, scale=(1, 1, 0.5), collider='box', parent = cam)
playerHandL = Entity(model='cube', color=color.yellow, scale=(1, 0.5, 0.5), collider='box', parent = cam)
playerHandR = Entity(model='cube', color=color.yellow, scale=(1, 0.5, 0.5), collider='box', parent = cam)
playerLegL = Entity(model='cube', color=color.green, scale=(1, 0.5, 0.5), collider='box', parent = cam)
playerLegR = Entity(model='cube', color=color.green, scale=(1, 0.5, 0.5), collider='box', parent = cam)
playerCheckGround = Entity(model="cube", color=color.green, scale=(1, 0.1, 0.5), collider='box', parent = cam)
worldGround = Entity(model='plane', texture='grass', scale=(1000, 0.1, 1000), collider='mesh')

def createPlayer():
    global playerHead
    global playerTorso
    global playerHandL
    global playerHandR
    global playerLegL
    global playerLegR
    global playerCheckGround
    global worldGround
    playerHead = Entity(model="cube", color=color.yellow, scale=0.6, collider='mesh', parent = cam)
    playerTorso = Entity(model="cube", color=color.blue, scale=(1, 1, 0.5), collider='box', parent = cam)
    playerHandL = Entity(model='cube', color=color.yellow, scale=(1, 0.5, 0.5), collider='box', parent = cam)
    playerHandR = Entity(model='cube', color=color.yellow, scale=(1, 0.5, 0.5), collider='box', parent = cam)
    playerLegL = Entity(model='cube', color=color.green, scale=(1, 0.5, 0.5), collider='box', parent = cam)
    playerLegR = Entity(model='cube', color=color.green, scale=(1, 0.5, 0.5), collider='box', parent = cam)
    playerCheckGround = Entity(model="cube", color=color.green, scale=(1, 0.1, 0.5), collider='box', parent = cam)
    worldGround = Entity(model='plane', color=color.gray, collider='mesh')
#------------СОЗДАНИЕ ИГРОКА------------

Sky() # Небо

playerTorso.position = (0, -0.75, 0) # тело, позиция

camera.position = (0, 2, -15)

worldGround.position = (0, -2.25, 0) # земля, позиция

playerCheckGround.position = (0, -2.2, 0)

playerHandL.position = (-0.75, -0.75, 0) # левая рука, позиция
playerHandL.rotation = (0, 0, 90) # левая рука, поворот
playerHandR.position = (0.75, -0.75, 0) # правая рука, позиция
playerHandR.rotation = (0, 0, 90) # правая рука, поворот

playerLegL.position = (-0.25, -1.75, 0) # левая нога, позиция
playerLegL.rotation = (0, 0, 90) # левая нога, поворот
playerLegR.position = (0.25, -1.75, 0) # правая нога, позиция
playerLegR.rotation = (0, 0, 90) # правая нога, поворот

def playerController(): # логика игрока
    global fallspeed # обьявлянем переменную

    #------------ФИЗИКА------------
    if playerCheckGround.intersects(worldGround).hit: # Если мы на земле то:
        fallspeed = 0
        isGround = 1
    if not playerCheckGround.intersects(worldGround).hit: # Если мы не на земле то:
        fallspeed += 0.01
        cam.position -= (0, fallspeed, 0)
        isGround = 0
    #------------ФИЗИКА------------


    #------------ПРЫЖОК------------
    if held_keys['space'] and isGround == 1: # Когда мы на земле и нажали на пробел:
        fallspeed -= 0.15
        cam.position -= (0, fallspeed, 0)
    #------------ПРЫЖОК------------

    if cam.position.y <= -10:
        cam.position = (0, 0, 0)
        isGround = True

    #------------ПЕРСПЕКТИВА------------
    if held_keys['v'] and isGround == 1: # Когда мы на земле и нажали на пробел:
        if isFirstCam == False:
            isFirstCam = True
        elif isFirstCam == True:
            isFirstCam = False
    #------------ПЕРСПЕКТИВА------------
def update(): # Все повторяется:
    if isFirstCam == True:
        camera.position = playerHead.position
    elif isFirstCam == False:
        camera.position = playerHead.position + (0, 2, -15)
    playerController()
    #listofplayers(str(playerPOS))

App.run() # иницилизируем игру