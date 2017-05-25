from gpiozero import Button
import pygame.mixer
from pygame.mixer import Sound
from signal import pause

pygame.mixer.init()

sound_pins = {
  25: Sound("./sounds/ach-i-wo.wav"),
  3: Sound("./sounds/ach-i-wo.wav"),
}

def prepareSounds():
  global sound_pins
  sound_pins = {
    25: Sound("./sounds/ach-i-wo.wav"),
    3: Sound("./sounds/ach-i-wo.wav"),
  }

prepareSounds()

buttons = [Button(pin) for pin in sound_pins]
for button in buttons:
  sound = sound_pins[button.pin.number]
  button.when_released = sound.play

pause()