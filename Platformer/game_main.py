#version 0.0.01a

#imports
import pygame, random, math, sys, configparser
from pygame.locals import *
pygame.init()

#defining color variables
Black = (  0,  0,  0)
White = (255,255,255)
Red   = (255,  0,  0)
Green = (  0,255,  0)
Blue  = (  0,  0,255)

#ConfigParser
config = configparser.ConfigParser()
config.read('config.ini')
def configSectionMap(section):
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

#resolution settings
xres = int(configSectionMap('Display') ['horizontalres'])
yres = int(configSectionMap('Display') ['verticalres'])

#window settings
fullscreenSet = configSectionMap('Display')['fullscreen']
if fullscreenSet == True:
	screen = pygame.display.set_mode((xres, yres), FULLSCREEN, DOUBLEBUF)
else:
	screen = pygame.display.set_mode((xres, yres), DOUBLEBUF)

#sprite classes
#class Player(pygame.sprite.Sprite):

#class Enemy(pygame.sprite.Sprite):

