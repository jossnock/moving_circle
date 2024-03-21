# Example file showing a basic pygame "game loop"
import pygame
import random
import math

# pygame setup
pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_COLOUR = "white"
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()
running = True
FPS = 60

# circle details
circle_centre_x = SCREEN_WIDTH // 2
circle_centre_y = SCREEN_HEIGHT // 2
circle_radius = 128

CIRCLE_MOVEMENT_ANGLE = math.pi / 4 # angle (in radians) clockwise from the horizontal that it starts at

circle_x_velocity = 0
circle_x_velocity_previous = 2

circle_y_velocity = 0
circle_y_velocity_previous = 2

circle_colour_1 = "white"
circle_colour_2 = (85, 85, 85)
circle_colour_3 = (170, 170, 170)
circle_colour_4 = "black"


circle_thickness = 4
COLOUR_INTERVAL = 48

# running
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a colour to wipe away anything from last frame
    SCREEN.fill(SCREEN_COLOUR)

    # renders the game
    for i in range(circle_radius // circle_thickness): # makes a multi-coloured circle and fills it with lines
        if i % 4 == 0:
            pygame.draw.circle(SCREEN, circle_colour_1, (circle_centre_x,circle_centre_y), circle_radius - (i * circle_thickness), circle_thickness, True)
            pygame.draw.circle(SCREEN, circle_colour_2, (circle_centre_x,circle_centre_y), circle_radius - (i * circle_thickness), circle_thickness, False, True)
            pygame.draw.circle(SCREEN, circle_colour_3, (circle_centre_x,circle_centre_y), circle_radius - (i * circle_thickness), circle_thickness, False, False, True)
            pygame.draw.circle(SCREEN, circle_colour_4, (circle_centre_x,circle_centre_y), circle_radius - (i * circle_thickness), circle_thickness, False, False, False, True)
        if i % 4 == 1:
            pygame.draw.circle(SCREEN, circle_colour_1, (circle_centre_x,circle_centre_y), circle_radius - (i * circle_thickness), circle_thickness, False, True)
            pygame.draw.circle(SCREEN, circle_colour_2, (circle_centre_x,circle_centre_y), circle_radius - (i * circle_thickness), circle_thickness, False, False, True)
            pygame.draw.circle(SCREEN, circle_colour_3, (circle_centre_x,circle_centre_y), circle_radius - (i * circle_thickness), circle_thickness, False, False, False, True)
            pygame.draw.circle(SCREEN, circle_colour_4, (circle_centre_x,circle_centre_y), circle_radius - (i * circle_thickness), circle_thickness, True)
        if i % 4 == 2:
            pygame.draw.circle(SCREEN, circle_colour_1, (circle_centre_x,circle_centre_y), circle_radius - (i * circle_thickness), circle_thickness, False, False, True)
            pygame.draw.circle(SCREEN, circle_colour_2, (circle_centre_x,circle_centre_y), circle_radius - (i * circle_thickness), circle_thickness, False, False, False, True)
            pygame.draw.circle(SCREEN, circle_colour_3, (circle_centre_x,circle_centre_y), circle_radius - (i * circle_thickness), circle_thickness, True)
            pygame.draw.circle(SCREEN, circle_colour_4, (circle_centre_x,circle_centre_y), circle_radius - (i * circle_thickness), circle_thickness, False, True)
        if i % 4 == 3:
            pygame.draw.circle(SCREEN, circle_colour_1, (circle_centre_x,circle_centre_y), circle_radius - (i * circle_thickness), circle_thickness, False, False, False, True)
            pygame.draw.circle(SCREEN, circle_colour_2, (circle_centre_x,circle_centre_y), circle_radius - (i * circle_thickness), circle_thickness, True)
            pygame.draw.circle(SCREEN, circle_colour_3, (circle_centre_x,circle_centre_y), circle_radius - (i * circle_thickness), circle_thickness, False, True)
            pygame.draw.circle(SCREEN, circle_colour_4, (circle_centre_x,circle_centre_y), circle_radius - (i * circle_thickness), circle_thickness, False, False, True)
    
    # keeping the velocity from before a stop
    if circle_x_velocity != 0:
        circle_x_velocity_previous = circle_x_velocity
    
    if circle_y_velocity != 0:
        circle_y_velocity_previous = circle_y_velocity

    # moving circle according to velocity
    circle_centre_x += circle_x_velocity
    circle_centre_y += circle_y_velocity

    # accelerates the circle
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_SPACE]):
        if circle_x_velocity_previous >= 0 and circle_y_velocity_previous >= 0:
            circle_x_velocity += 1
            circle_y_velocity += 1
        if circle_x_velocity_previous >= 0 and circle_y_velocity_previous < 0:
            circle_x_velocity += 1
            circle_y_velocity -= 1
        if circle_x_velocity_previous < 0 and circle_y_velocity_previous >= 0:
            circle_x_velocity -= 1
            circle_y_velocity += 1
        if circle_x_velocity_previous < 0 and circle_y_velocity_previous < 0:
            circle_x_velocity -= 1
            circle_y_velocity -= 1

    # deccelerates the circle
    if (keys[pygame.K_BACKSPACE]):
        if circle_x_velocity != 0:
            if circle_x_velocity > 0:
                circle_x_velocity -= 1
            elif circle_x_velocity < 0:
                circle_x_velocity += 1
        if circle_y_velocity != 0:
            if circle_y_velocity > 0:
                circle_y_velocity -= 1
            elif circle_y_velocity < 0:
                circle_y_velocity += 1
    
    def randomise_colours(interval):
        """Pass in the interval you want the colours to vary by (0 <= interval <= 255))
        Randomises circle_colour_1, 2, 3, and 4
        Each colour's red value should be similar to the other colour's red values, same for green and blue"""
        random_colour_r = random.randint(0 + interval, 255 - interval)
        random_colour_g = random.randint(0 + interval, 255 - interval)
        random_colour_b = random.randint(0 + interval, 255 - interval)
        global circle_colour_1
        circle_colour_1 = (random_colour_r + random.randint(-interval, interval), random_colour_g + random.randint(-interval, interval), random_colour_b + random.randint(-interval, interval))
        global circle_colour_2
        circle_colour_2 = (random_colour_r + random.randint(-interval, interval), random_colour_g + random.randint(-interval, interval), random_colour_b + random.randint(-interval, interval))
        global circle_colour_3
        circle_colour_3 = (random_colour_r + random.randint(-interval, interval), random_colour_g + random.randint(-interval, interval), random_colour_b + random.randint(-interval, interval))
        global circle_colour_4
        circle_colour_4 = (random_colour_r + random.randint(-interval, interval), random_colour_g + random.randint(-interval, interval), random_colour_b + random.randint(-interval, interval))

    # bounces if it hits an edge and randomises the circle colours
    if circle_centre_x + circle_radius >= SCREEN_WIDTH or circle_centre_x - circle_radius <= 0:
        circle_x_velocity = -circle_x_velocity
        randomise_colours(COLOUR_INTERVAL)
    if circle_centre_y + circle_radius >= SCREEN_HEIGHT or circle_centre_y - circle_radius <= 0:
        circle_y_velocity = -circle_y_velocity
        randomise_colours(COLOUR_INTERVAL)
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    CLOCK.tick(FPS)

pygame.quit()




