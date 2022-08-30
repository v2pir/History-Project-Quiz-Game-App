#The ptext file is not mine...I am using it to help display text on pygame display. 
#Click on the link at the top in the ptext.py file to see the creator's repository

#Vansh Chhabra

#8/30/2022

#Mansa Musa and Mali Quiz Game

#Version 1.0 (This will probably be the only version)

#If you want to use this program and post it somewhere, please give me credit

import pygame
import random
import ptext
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Mansa Musa and Mali")

blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
purple = (255,0,255)
black = (0,0,0)
white = (255,255,255)
yellow = (255,255,0)
orange = (255,128,0)
aqua = (0,204,204)
pink = (175,0,175)
grey = (127.5, 127.5, 127.5)

colors = [blue, red, green, purple, white, yellow, orange, aqua, pink]
width = random.randint(50,100)
height = random.randint(50,100)

def string_chunks(string, x):
    lstring = string.split()
    new_list = []
    counter = 0
    for word in lstring:
        if counter%x == 0 and counter!= 0:
            word += "\n"
        counter += 1
        new_list.append(word)
    new = " ".join(new_list)
    return new

#comic sans text
def show_text_cs(msg, pos, color):
    x, y = pos
    if 20*(len(msg)) + x > screen.get_width():
        average = 5
        char_per_line = (screen.get_width())/(17)
        char_per_line = int(char_per_line)
        word_per_line = int(char_per_line/average)
        text = string_chunks(msg, word_per_line - 2)
        ptext.draw(text, pos, sysfontname="comicsansms", color= color, fontsize = 25)
    else:
        ptext.draw(msg, pos, sysfontname="comicsansms", color= color, fontsize = 25)

def show_text_arial(msg, pos, color):
    x, y = pos
    if 20*(len(msg)) + x > screen.get_width():
        average = 5
        char_per_line = (screen.get_width())/(17)
        char_per_line = int(char_per_line)
        word_per_line = int(char_per_line/average)
        text = string_chunks(msg, word_per_line - 2)
        ptext.draw(text, pos, sysfontname="arial", color= color, fontsize = 25)
    else:
        ptext.draw(msg, pos, sysfontname="arial", color= color, fontsize = 25)

def button(msg, dimensions, position, color, text_color):
    width, height = dimensions
    x, y = position
    pygame.draw.rect(screen,color,[x,y,width,height])
    fontobj = pygame.font.SysFont("arial", 15)
    msgobj = fontobj.render(msg, False, text_color)
    screen.blit(msgobj,(x+5,y+5))

#questions and answer
questions = {"What did Mansa Musa make to leave a lasting impression in Mecca?": "pilgrimage", "What was the name of Mali's founding ruler?": "Sundiata", "What religion did Mali's founding ruler believe in?": "Islam", "Who did Sundiata establish trade relationships with?": "merchants", "What was the most powerful of the new trading societies that had risen from the fall of Ghana": "Mali"}

q = list(questions.keys())

len_keys = len(questions)

text_color = green

#picking index of random question in "questions"
m = random.randint(0, len_keys-1)

#the question
sentence = q[m]

length = 0

word = ''

#participants
people = 0

names = 'Vansh Chhabra'

#game loop
while True:

    while people != 1:
        pygame.display.update()
        show_text_arial(names, (100, 200), yellow)
        show_text_arial("Mansa Musa and Mali", (200, 400), purple)
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                people = 1

    #clear screen
    screen.fill(black)
   
    #draw all items

    dashes = ("_ " * len(questions[sentence]))

    #show question
    show_text_cs(sentence, (30, 100), grey)

    #showing number of letters in answer
    show_text_cs(dashes, (30, 300), grey)

    #covering up _ after guessing letter for that place
    show_text_cs(dashes[:(length*2)], (30, 300), black)

    word1 = [*word]
    word1 = " ".join(word1)

    #the actual guessing
    show_text_cs(word1 + "|", (30, 300), text_color)

    if word == questions[sentence]:
        screen.fill(black)
        button("Play Again", (125, 40), (200,300) , aqua, yellow)
        button("Quit", (125,40), (500,300) , pink, yellow)
        answer = ""
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 200 <= mouse_x and mouse_x <= 325 and 300 <= mouse_y and mouse_y <= 340:
                    answer = "continue"
                elif 500 <= mouse_x and mouse_x <= 625 and 300 <= mouse_y and mouse_y <= 340:
                    answer = "quit"
        if answer == "continue":
            new = random.randint(0, len_keys-1)
            sentence = q[new]
            word = ""
            length = 0
            continue
        elif answer == "quit":
            break


    #check for events and change statuses/variables
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            #shift 0-9
            if event.key == pygame.K_1 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                word += "!"
            elif event.key == pygame.K_2 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                word += "@"
            elif event.key == pygame.K_3 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                word += "#"
            elif event.key == pygame.K_4 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                word += "$"
            elif event.key == pygame.K_5 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                word += "%"
            elif event.key == pygame.K_6 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                word += "^"
            elif event.key == pygame.K_7 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                word += "&"
            elif event.key == pygame.K_8 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                word += "*"
            elif event.key == pygame.K_9 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                word += "("
            elif event.key == pygame.K_0 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                word += ")"
            #rest of the special symbols
            elif event.key == pygame.K_COMMA and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                word += "<"
            elif event.key == pygame.K_PERIOD and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                word += ">"
            elif event.key == pygame.K_SLASH and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                word += "?"
            elif event.key == pygame.K_SEMICOLON and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                word += ":"
            elif event.key == pygame.K_QUOTEDBL and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                word += '"'
            ##uppercase
            elif (event.key >= 97 and event.key <= 123) and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                letter = chr(event.key - 32)
                word += letter
            #lowercase
            elif (event.key >= 48 and event.key <=56) or (event.key >= 97 and event.key <= 123):
                letter = chr(event.key)
                word += letter
            #more special symbols
            elif event.key == 8:
                word = word[:-1]
            elif event.key == pygame.K_SPACE:
                word += " "
            elif event.key == pygame.K_PERIOD:
                word += "."
            elif event.key == pygame.K_COMMA:
                word += ","
            elif event.key == pygame.K_SLASH:
                word += "/"
            elif event.key == pygame.K_BACKSLASH:
                word += "\\"
            elif event.key == pygame.K_SEMICOLON:
                word += ";"
            elif event.key == pygame.K_RETURN:
                word += "\n"
            elif event.key == pygame.K_QUOTE:
                word += "'"
            elif event.key == 45:
                word += "-"

            length = len(word)

            if word == (questions[sentence])[:length]:
                text_color = green
                continue
            else:
                text_color = red

            #insert "do you want to place again" stuff here

    #update
    pygame.display.update()