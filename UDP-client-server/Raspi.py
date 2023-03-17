import picamera
from time import sleep
import datetime as dt
from gpiozero import MotionSensor
from signal import pause
import base64
import socket
from json import dumps
import time
import os
import zipfile

pir = MotionSensor(4)

camera = picamera.PiCamera()
camera.start_preview()

frame = 1
i = 0

out_zip_file = "compressedTest.jpg"

while i<6:
        imagename = '/home/bigpopa/videos/testimage.jpg'

        pir.wait_for_motion()
        print("Motion detected!")
        print(i)
        i += 1
        try:
                camera.capture(imagename)
                time.sleep(3)

        finally:
                camera.stop_preview()
                print('Picture taken!')
                camera.close()


        compression = zipfile.ZIP_DEFLATED
        zf = zipfile.ZipFile(out_zip_file, mode = "w")
        try:
                for file_to_write in imagename:
                        zf.write(file_to_write, file_to_write, compress_type=compression)

        except FileNotFoundError as e:
                print(f' * Exception occured during zip process - {e}')

        finally:
                zf.close()

        #Sends the file to server via TCP
        with open(imagename, "rb") as images:
                imagesToString = base64.b64encode(images.read())
                base64_string = imagesToString.decode("utf-8")
                raw_data = {"image1": base64_string}
                json_data = dumps(raw_data)

        print(json_data)
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        clientSocket.connect((socket.gethostname(), 13000))
        clientSocket.send(json_data.encode())

        os.remove(imagename)
        print("The file has been removed")
