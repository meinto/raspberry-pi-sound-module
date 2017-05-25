from gpiozero import Button
from signal import pause

button = Button(25)

def printPressedState():
  global button
  print('is_pressed ' + str(button.is_pressed))

button.when_pressed = printPressedState
button.when_released = printPressedState

pause()