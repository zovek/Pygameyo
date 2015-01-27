#version 0.0.01a

#imports
import pygame, random, math, sys
from pygame.locals import *
pygame.init()

#defining color variables
Black = (  0,  0,  0)
White = (255,255,255)
Red   = (255,  0,  0)
Green = (  0,255,  0)
Blue  = (  0,  0,255)

#resolution settings
aspectRatio = aspectRatio1
res = res1
fullscreen = (False)
aspectRatio1 = ('16:9')
aspectRatio2 = ('16:10')
if aspectRatio == aspectRatio1:
	if res == res1:
		xres = (1280)
		yres = (720)
		resScale = (1)
	elif res == res2:
		xres = (1920)
		yres = (1080)
		resScale = (1.5)
	elif res == res3:
		xres = (2560)
		yres = (1440)
		resScale = (2)
	elif res == res4:
		xres = (3840)
		yres = (2160)
		resScale = (3)
elif aspectRatio == aspectRatio2:
	if res == res1:
		xres = (1280)
		yres = (800)
		resScale = (1)
	elif res == res2:
		xres = (1920)
		yres = (1200)
		resScale = (1.5)
	elif res == res3:
		xres = (2560)
		yres = (1600)
		resScale = (2)
	elif res == res4:
		xres = (3840)
		yres = (2400)
		resScale = (3)
