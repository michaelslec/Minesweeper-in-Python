import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Minesweeper!')

crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event)

    pygame.display.update()

pygame.quit()
quit()