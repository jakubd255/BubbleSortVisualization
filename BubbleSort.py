import pygame
import time
import sys
import random

#DEFINITIOS AND GLOBALS############################################################################

elements=100
column_length=10
window_height=480

pygame.init()
window=pygame.display.set_mode((elements*column_length,window_height))
pygame.display.set_caption('Sorting alorithms visualization')

color_green=pygame.Color(57, 226, 173)
color_swapped=pygame.Color(22, 92, 80)
color_white=pygame.Color(255, 255, 255)

#List for random values
list=[]
for i in range(0, elements):
    list.append(random.randint(1, 100))


#FUNCTIONS########################################################################################

#Drawing------------------------------------
def draw(b):
    global list
    global elements
    global window

    window.fill(color_white)

    #Column drawing
    for i in range(0, elements):
        height=4*list[i]
        column=pygame.rect.Rect(i*column_length,window_height-height,column_length,height)

        if b==i:
            pygame.draw.rect(window, color_swapped, column)
        else: 
            pygame.draw.rect(window, color_green, column)
    
    #Time waiting
    #time.sleep(0.01)
    #Refreshing 
    pygame.display.update()


#Bubble sort--------------------------------
#Value swapping
def swap(a):
    global list
    temp=list[a]
    list[a]=list[a+1]
    list[a+1]=temp

    button_input()
    draw(a+1)
    

#Comparing
def bubble_sort():
    global list
    global elements

    for i in range(0, elements):
        for j in range(0, elements-i-1):
            if list[j]>list[j+1]:
                swap(j)


#Control buttons input----------------------
def button_input():
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


#MAIN PROGRAM################################################################################

while True:
    window.fill(color_white)
    button_input()
    draw(-5)
    bubble_sort()
    pygame.display.update()