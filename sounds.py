from gpiozero import Button
import pygame.mixer
from pygame.mixer import Sound
from signal import pause
from subprocess import check_call
import functools
from random import randint

pygame.mixer.init()

# switches:
# GP 8
# GP 11
# --- not used yet:
# GP 25
# GP 9
sound_switch = 1

def switchSounds(): 
  global sound_switch
  if (Button(8).is_pressed === true and Button(11).is_pressed === true):
    sound_switch = 1
  if (Button(8).is_pressed === true and Button(11).is_pressed === false):
    sound_switch = 2
  if (Button(8).is_pressed === false and Button(11).is_pressed === true):
    sound_switch = 3
  if (Button(8).is_pressed === false and Button(11).is_pressed === false):
    sound_switch = 4
    

Button(8).when_released = switchSounds
Button(8).when_pressed = switchSounds
Button(11).when_released = switchSounds
Button(11).when_pressed = switchSounds

# sound buttons:
# GP 4 -> random!
# GP 14
# GP 15
# GP 18
# GP 17
random_sound_pool = {
  1: Sound("./sounds/ach-i-wo.wav"),
  2: Sound("./sounds/alles-quatsch.wav"),
}

sound_pins = {
  1: {
    14: Sound("./sounds/ach-i-wo.wav"),
    15: Sound("./sounds/ach-i-wo.wav"),
    18: Sound("./sounds/ach-i-wo.wav"),
    17: Sound("./sounds/ach-i-wo.wav"),
  },
  2: {
    14: Sound("./sounds/ach-i-wo.wav"),
    15: Sound("./sounds/ach-i-wo.wav"),
    18: Sound("./sounds/ach-i-wo.wav"),
    17: Sound("./sounds/ach-i-wo.wav"),
  },
  3: {
    14: Sound("./sounds/ach-i-wo.wav"),
    15: Sound("./sounds/ach-i-wo.wav"),
    18: Sound("./sounds/ach-i-wo.wav"),
    17: Sound("./sounds/ach-i-wo.wav"),
  },
  4: {
    14: Sound("./sounds/ach-i-wo.wav"),
    15: Sound("./sounds/ach-i-wo.wav"),
    18: Sound("./sounds/ach-i-wo.wav"),
    17: Sound("./sounds/ach-i-wo.wav"),
  },
}

def playRandomSound():
  global random_sound_pool
  random_nr = randint(1, 2)
  sound = random_sound_pool[random_nr]
  sound.play()

def playDefinedSound(pin_number):
  global sound_pins
  global sound_switch
  global playSound
  sound = sound_pins[sound_switch][pin_number]
  sound.play()

Button(4).when_released = playRandomSound
buttons = [Button(pin) for pin in sound_pins]
for button in buttons:
  button.when_released = functools.partial(playDefinedSound, button.pin.number) 

# shutdown button:
# GP 10
def shutdown():
  check_call(['sudo', 'poweroff'])

shutdownButton = Button(17, hold_time=2)
shutdownButton.when_held = shutdown

pause()