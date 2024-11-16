import pygame

pygame.init()

window_size = (640, 480)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("My First Game Screen")

white = (255, 255, 255)
custom_colour = (0, 128, 255)

font = pygame.font.Font(None, 74)
text = font.render("Hello, Pygame!", True, custom_colour)
text_rect = text.get_rect(center=(window_size[0] // 2, window_size[1] // 3))

rectangle_x = 200
rectangle_y = 250
rectangle_height = 100
rectangle_width = 240

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)
    pygame.draw.rect(screen, custom_colour, pygame.Rect(rectangle_height,rectangle_width,rectangle_x,rectangle_y))
    screen.blit(text, text_rect)
    pygame.display.flip()

pygame.quit()