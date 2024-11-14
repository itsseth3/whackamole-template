import random
import pygame

def draw_grid(screen):
    for i in range(0, 640, 32):
        pygame.draw.line(screen, 'black', (i, 0), (i, 512))
    for j in range(0, 512, 32):
        pygame.draw.line(screen, 'black', (0, j), (640, j))

def mole_movement(screen, image, destination):
    screen.blit(image, image.get_rect(topleft=destination))

def main():
    try:
        pygame.init()
        random_destination = (random.randrange(0, 640, 32), random.randrange(0, 512, 32))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (random_destination[0] <= event.pos[0] <= random_destination[0]+31) and (random_destination[1 >= event.pos[1] >= random_destination[1]+31]):
                        random_destination = (random.randrange(0, 640, 32), random.randrange(0, 512, 32))
            screen.fill("light blue")
            draw_grid(screen)
            mole_movement(screen, mole_image, random_destination)
            pygame.display.flip()
            clock.tick(60)
            screen.blit(mole_image, mole_image.get_rect(topleft = (32, 32)))
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
