"""
Controls:
SPACE to speed up
BACKSPACE to slow down
, to enable light mode
. to enable dark mode
= to enable trail
- to disable and clear trail
"""

import random
import math
import pygame

# pygame setup
pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen_colour = "white"
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()
running = True
FPS = 60

# circle details
circle_centre_x = SCREEN_WIDTH // 2
circle_centre_y = SCREEN_HEIGHT // 2
circle_radius = 128
circle_thickness = 4

circle_colour_1 = "white"
circle_colour_2 = (85, 85, 85)
circle_colour_3 = (170, 170, 170)
circle_colour_4 = "black"
COLOUR_INTERVAL = 48

is_trail_visible = False

INITIAL_CIRCLE_X_VELOCITY_SIGN = 1
INITIAL_CIRCLE_Y_VELOCITY_SIGN = 1
CIRCLE_X_VELOCITY_MULTIPLIER = 1
CIRCLE_Y_VELOCITY_MULTIPLIER = 1

CIRCLE_MOVEMENT_ANGLE = (1/4) * math.pi # angle (in radians) clockwise from the horizontal that the circle starts moving at

# circle velocity calculations; if angle > pi/2, a change of sign is required; if angle == pi/2 or 3pi/2, x velocity = 0
if ((3/2) * math.pi) < CIRCLE_MOVEMENT_ANGLE <= (2 * math.pi): # 1st quadrant
    CIRCLE_Y_VELOCITY_MULTIPLIER = round(math.tan(CIRCLE_MOVEMENT_ANGLE), 3)
    INITIAL_CIRCLE_Y_VELOCITY_SIGN = -1
if (math.pi) <= CIRCLE_MOVEMENT_ANGLE < ((3/2) * math.pi): # 2nd quadrant
    CIRCLE_Y_VELOCITY_MULTIPLIER = round(math.tan(CIRCLE_MOVEMENT_ANGLE), 3)
    INITIAL_CIRCLE_Y_VELOCITY_SIGN = -1
    INITIAL_CIRCLE_X_VELOCITY_SIGN = -1
if (math.pi / 2) < CIRCLE_MOVEMENT_ANGLE <= (math.pi): # 3rd quadrant
    CIRCLE_Y_VELOCITY_MULTIPLIER = round(math.tan(CIRCLE_MOVEMENT_ANGLE), 3)
    INITIAL_CIRCLE_X_VELOCITY_SIGN = -1
if 0 <= CIRCLE_MOVEMENT_ANGLE < (math.pi / 2): # 4th quadrant
    CIRCLE_Y_VELOCITY_MULTIPLIER = round(math.tan(CIRCLE_MOVEMENT_ANGLE), 3)
if CIRCLE_MOVEMENT_ANGLE == (math.pi / 2):
    CIRCLE_X_VELOCITY_MULTIPLIER = 0
if CIRCLE_MOVEMENT_ANGLE == ((3/2) * math.pi):
    CIRCLE_X_VELOCITY_MULTIPLIER = 0
    INITIAL_CIRCLE_Y_VELOCITY_SIGN = -1
circle_x_velocity = 0
circle_x_velocity_previous =  2 * INITIAL_CIRCLE_X_VELOCITY_SIGN * CIRCLE_X_VELOCITY_MULTIPLIER
circle_y_velocity = 0
circle_y_velocity_previous =  2 * INITIAL_CIRCLE_Y_VELOCITY_SIGN * CIRCLE_Y_VELOCITY_MULTIPLIER



# running
while running:
    keys = pygame.key.get_pressed()

    # change background colour
    if (keys[pygame.K_COMMA]):
        screen_colour = "white"
    if (keys[pygame.K_PERIOD]):
        screen_colour = "black"
    
    # toggle circle trail
    if (keys[pygame.K_EQUALS]):
        is_trail_visible = True
    if (keys[pygame.K_MINUS]):
        is_trail_visible = False

    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a colour to wipe away anything from last frame
    if is_trail_visible == False:
        SCREEN.fill(screen_colour)

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
    
    if round(circle_y_velocity, 3) != 0:
        circle_y_velocity_previous = circle_y_velocity

    # moving circle according to velocity
    circle_centre_x += circle_x_velocity
    circle_centre_y += circle_y_velocity

    # accelerates the circle
    if (keys[pygame.K_SPACE]):
        if circle_x_velocity_previous >= 0 and round(circle_y_velocity_previous, 3) >= 0:
            circle_x_velocity += CIRCLE_X_VELOCITY_MULTIPLIER
            circle_y_velocity += CIRCLE_Y_VELOCITY_MULTIPLIER
        if circle_x_velocity_previous >= 0 and round(circle_y_velocity_previous, 3) < 0:
            circle_x_velocity += CIRCLE_X_VELOCITY_MULTIPLIER
            circle_y_velocity -= CIRCLE_Y_VELOCITY_MULTIPLIER
        if circle_x_velocity_previous < 0 and round(circle_y_velocity_previous, 3) >= 0:
            circle_x_velocity -= CIRCLE_X_VELOCITY_MULTIPLIER
            circle_y_velocity += CIRCLE_Y_VELOCITY_MULTIPLIER
        if circle_x_velocity_previous < 0 and round(circle_y_velocity_previous, 3) < 0:
            circle_x_velocity -= CIRCLE_X_VELOCITY_MULTIPLIER
            circle_y_velocity -= CIRCLE_Y_VELOCITY_MULTIPLIER

    # deccelerates the circle
    if (keys[pygame.K_BACKSPACE]):
        if circle_x_velocity != 0:
            if circle_x_velocity > 0:
                circle_x_velocity -= CIRCLE_X_VELOCITY_MULTIPLIER
            elif circle_x_velocity < 0:
                circle_x_velocity += CIRCLE_X_VELOCITY_MULTIPLIER
        if round(circle_y_velocity, 3) != 0:
            if circle_y_velocity > 0:
                circle_y_velocity -= CIRCLE_Y_VELOCITY_MULTIPLIER
            elif circle_y_velocity < 0:
                circle_y_velocity += CIRCLE_Y_VELOCITY_MULTIPLIER
    
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

