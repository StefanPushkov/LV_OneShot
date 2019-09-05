import socket
import cv2
import time
import getpass
from time import gmtime, strftime
import os



timeout = 10
host = 'localhost'
port = 8089
addr = (host, port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(addr)
server.listen()


def take_shot():
    getUser = getpass.getuser()
    save = 'C:/Users/' + getUser + "/Desktop/Web_cam_shots"
    print(save)
    # Заменять код для нескольких камер, начиная отсюда (пример патча ниже)
    camera_port = 0
    camera = cv2.VideoCapture(camera_port)
    #time.sleep(0.1)
    return_value, image = camera.read()

    #new_file_name = strftime("%Y_%m_%d_%H_%M_%S", gmtime())
    new_path = os.path.join(save, "photo.png")
    cv2.imwrite(new_path, image)
    return new_path
    # Заканчивая здесь




while True:
    conn, address = server.accept()
    cmnd = conn.recv(9)
    print(cmnd)

    if 'PLAY' in str(cmnd):
        path = take_shot()
        #with open(path, 'rb') as f:
           # bytes = f.read()
        #b = bytes
        conn.sendall(b'OKAY')
       # conn.send(bytearray(str(bytes), 'utf-8'))

#server.close()







#   Приведенный ниже код должен работать
#   К примеру, если использовать две камеры: 1 веб-камеру, а другую - USB-камеру


#   cam1_port = 0
#   cam2_usb_port = 1
#   cam1 = cv2.VideoCapture(cam1_port)
#   cam2_usb = cv2.VideoCapture(cam2_usb_port)
#   time.sleep(0.1)

#   return_value_cam1, image1 = cam1.read()
#   return_value_cam2_usb, image2 = cam2_usb.read()

#   new_file_name_1 = strftime("%Y_%m_%d_%H_%M_%S", gmtime())
#   new_file_name_2 = strftime("%Y_%m_%d_%H_%M_%S", gmtime())
#   cv2.imwrite(os.path.join(save, new_file_name_1 + ".png"), image1)
#   cv2.imwrite(os.path.join(save, new_file_name_2 + ".png"), image2)








