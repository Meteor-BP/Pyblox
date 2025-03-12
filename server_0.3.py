import socket
 
server = socket.socket()            # создаем объект сокета сервера
hostname = socket.gethostname()     # получаем имя хоста локальной машины
port = 12345                        # устанавливаем порт сервера
server.bind((hostname, port))       # привязываем сокет сервера к хосту и порту
server.listen(5)                    # начинаем прослушиваение входящих подключений
players = {}
print("Сервер включен...")
while True:
    con, _ = server.accept()     # принимаем клиента
    data = con.recv(1024)           # получаем данные от клиента
    message = data.decode()         # преобразуем байты в строку

    print(f"Сообщение от клиента: {message}")
    if str(message) not in str(players):
        players["ID"] = str(message)
    print("Актуальный список игроков:" + str(players))
    message = str(players)       # инвертируем строку
    con.send(message.encode())      # отправляем сообщение клиенту
    players.clear()