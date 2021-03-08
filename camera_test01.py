import time
import picamera

print("Running..")

with picamera.PiCamera() as camera:
  camera.resolution = (1024, 768) # tells the computer the resolution to expect from the camera
  camera.start_preview()
  time.sleep(2)
  camera.capture('camera_test.jpg') # takes a picture and saves it as camera_test.jpg
  print("Done.")