import cv2
import numpy as np
import time

# recorte de micrografias de fibra de un procesamiento del ofda 2000
# detectar frame ini y frame stop
# recorrer los frames e imprimir nro de frame
  # imprimir nro de frame
video_capture = cv2.VideoCapture("captura.mp4")

start_frame = 157
stop_frame = 445

numFrame = 0

y = 74
h = 198
x = 1175
w = 190

while(video_capture.isOpened()):
    ret, frame = video_capture.read()
    if ret == False:
        break

    if numFrame >= start_frame:
      #if numFrame == start_frame:
      #  cv2.imwrite("frame0.png", frame)
      time.sleep(1/10)
      #frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
      frame = frame[y:y+h, x:x+w]
      cv2.imwrite("ofda/" + str(numFrame).zfill(4) + ".png", frame)

      cv2.putText(frame, "Frame:" + str(numFrame), (50,50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0))
      cv2.imshow("Tracking", frame)

    if(numFrame == stop_frame):
      break
    #time.sleep(1)
    numFrame+=1
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

video_capture.release()
cv2.destroyAllWindows()


# desde que aparece el frame con fibra hasta el ultimo frame con fibra (frame ini, frame stop)
  # guardar imagen

