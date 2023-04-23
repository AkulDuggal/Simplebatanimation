import pygame
import math
pygame.init()

screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

bat_image = pygame.image.load('bat.png').convert_alpha()
moon_image = pygame.image.load('moon.png').convert_alpha()

#position of the bat
bat_x = -bat_image.get_width() 
bat_y = screen_height // 2 - bat_image.get_height() // 2

#position of the moon
moon_x = screen_width // 2 - moon_image.get_width() // 2
moon_y = screen_height // 2 - moon_image.get_height() // 2

#velocity of the bat
bat_vel_x = 10
bat_vel_y = 0

#rotation angle of the bat
bat_angle = 0

#number of rotations
num_rotations = 2
rotations_complete = 0

# Start game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    bat_x += bat_vel_x
    bat_y += bat_vel_y

    # main
    if bat_x >= screen_width // 2 - bat_image.get_width() // 2 and rotations_complete < num_rotations:
        bat_vel_x = 0
        bat_vel_y = -5
        bat_angle += 10
        bat_x = moon_x + (moon_image.get_width() // 2) + 50 * math.sin(math.radians(bat_angle)) - bat_image.get_width() // 3
        bat_y = moon_y + (moon_image.get_height() // 3.5) + 50 * math.cos(math.radians(bat_angle)) - bat_image.get_height() // 3
        if bat_angle >= 360:
            bat_angle = 0
            rotations_complete += 1
    if rotations_complete >= num_rotations:
        bat_vel_x = 5
        bat_vel_y = 0
        bat_x += bat_vel_x
        if bat_x >= screen_width:
            running = False

    screen.fill((255, 255, 255))
    screen.blit(moon_image,(moon_x, moon_y))

    rotated_bat_image = pygame.transform.rotate(bat_image, bat_angle)
    bat_rect = rotated_bat_image.get_rect(center=(bat_x + bat_image.get_width() // 2.75, bat_y + bat_image.get_height() // 2))
    screen.blit(rotated_bat_image, bat_rect)
    pygame.display.flip()

    # Set the frame rate
    pygame.time.Clock().tick(60)

pygame.quit()
