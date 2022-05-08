# -*- coding: utf-8 -*-
import pygame
import os
import sys

from pygame.table import Board

board = Board(7, 6)
running = True
board.coord()
screen = pygame.display.set_mode((600, 500))
image = pygame.image.load("a.jpg")
image1 = pygame.transform.scale(image, (700, 700))
screen.blit(image1, (0, 0))

board.render(screen)
pygame.display.flip()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            coord = board.on_click(board.get_cell(event.pos))

            print(coord)
            color1 = screen.get_at(pygame.mouse.get_pos())
            # print(color1)
            board.color(screen, coord, color1)
            # pygame.display.flip()
