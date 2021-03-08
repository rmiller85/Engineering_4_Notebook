import time
import picamera

print("Picture 1..")

with picamera.PiCamera() as camera:
  camera.resolution = (1024, 768) # tells the computer the resolution to expect from the camera
  camera.image_effect = 'solarize'
  camera.start_preview()
  time.sleep(2)
  camera.capture('picture1.jpg')

print("Picture 2..")

with picamera.PiCamera() as camera:
  camera.resolution = (1024, 768) # tells the computer the resolution to expect from the camera
  camera.image_effect = 'oilpaint'
  camera.start_preview()
  time.sleep(2)
  camera.capture('picture2.jpg')

print("Picture 3..")

with picamera.PiCamera() as camera:
  camera.resolution = (1024, 768) # tells the computer the resolution to expect from the camera
  camera.image_effect = 'washedout'
  camera.start_preview()
  time.sleep(2)
  camera.capture('picture3.jpg')

print("Picture 4..")

with picamera.PiCamera() as camera:
  camera.resolution = (1024, 768) # tells the computer the resolution to expect from the camera
  camera.image_effect = 'colorswap'
  camera.start_preview()
  time.sleep(2)
  camera.capture('picture4.jpg')

print("Picture 5..")

with picamera.PiCamera() as camera:
  camera.resolution = (1024, 768) # tells the computer the resolution to expect from the camera
  camera.image_effect = 'gpen'
  camera.start_preview()
  time.sleep(2)
  camera.capture('picture5.jpg')