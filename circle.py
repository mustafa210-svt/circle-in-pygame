import pygame

# Screen dimensions and title
WIDTH = 600
HEIGHT = 600
TITLE = "Circle"

# Initialize Pygame
pygame.init()

# Creating the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Creating the title
pygame.display.set_caption(TITLE)

# Circle class
class Circle:
    def __init__(self, x, y, radius, colour):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour

    def draw(self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.radius)

# Create an instance of Circle
circle1 = Circle(100, 200, 30, (0, 255, 0))  # Changed "green" to RGB tuple

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get mouse position and update circle's position
            circle1.x, circle1.y = pygame.mouse.get_pos()

    # Clear the screen
    screen.fill("white")
    
    # Draw the circle
    circle1.draw()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
