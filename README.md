# circle_bouncing

Renders a moving circle using pygame.

## Features

- The circle bounces back when it hits the edge

- The circle is made up of stripes of 4 different colours

- Randomises circle colours when it bounces, with the 4 different colours within an interval of RGB values (i.e. they don't contrast with eachother too much)

## Initial Inputs

- Circle radius (default is 128

- Circle thickness (default is radius DIV 32)

- Circle acceleration (default is 1)

- Circle movement angle (in radians) (default is pi/4)

## Controls

- Press SPACE to speed up the circle

- Press BACKSPACE to slow down the circle

- Press , to enable light mode (default) (will clear trail when enabled)

- Press . to enable dark mode (will clear trail when enabled)

- Press = to enable trail

- Press - to disable and clear trail

## Todo

- Fix circle movement angle changer

- Add capability for angles smaller than 0 and larger than 2 pi
