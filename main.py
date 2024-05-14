import pygame
from world import *
from button import Button

def get_list_of_coordinates(up, down):
    # first determine if it's a horizontal line or vertical
    x_diff = abs(up[0] - down[0])
    y_diff = abs(up[1] - down[1])
    if x_diff > y_diff:
        print("Horizontal")
    else:
        print("Vertical")


# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Courier New', 14)
save_file_message = my_font.render("Enter your world name:", True, (0, 0, 0))
pygame.display.set_caption("Escape Devarque Level Creator")

# set up variables for the display
SCREEN_HEIGHT = 780
SCREEN_WIDTH = 1300
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

r = 255
g = 255
b = 255

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
world = World()
save_button = Button("save", 1000, 110)
load_button = Button("load", 1150, 110)

# creating text box rectangle, color, and whether it's active or not
text_box = pygame.Rect(1000, 50, 280, 40)
text_box_color = (0, 0, 0)
text_box_active = False

# this is String that will go in the text box
file_name = ""
file_name_message = my_font.render(file_name, True, (0, 0, 0))
clicked_down_coordinate = (0, 0)
clicked_up_coordinate = (0, 0)

# -------- Main Program Loop -----------
while run:

    # --- Main event loop
    ## ----- NO BLIT ZONE START ----- ##
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

        if event.type == pygame.KEYUP and text_box_active:
            # if the user presses backspace, remove the last letter from the text
            if event.key == 8:
                file_name = file_name[0:len(file_name)-1]
                file_name_message = my_font.render(file_name, True, (0, 0, 0))
            # otherwise, add the typed letter to the text field
            else:
                file_name += event.unicode
                file_name_message = my_font.render(file_name, True, (0, 0, 0))

        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked_down_coordinate = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            clicked_up_coordinate = event.pos

            if clicked_up_coordinate != clicked_down_coordinate:
                get_list_of_coordinates(clicked_up_coordinate, clicked_down_coordinate)
            # activate the text box
            if text_box.collidepoint(event.pos):
                text_box_color = (0, 0, 255)
                text_box_active = True
            # de-activate the text box
            else:
                text_box_color = (0, 0, 0)
                text_box_active = False

            if save_button.rect.collidepoint(event.pos):
                world.save_world(file_name)

            if load_button.rect.collidepoint(event.pos):
                world.load_world(file_name)

            row, column = world.get_clicked_tile(event.pos)
            if event.button == 1:
                world.world_map[row][column].switch_tile()
            if event.button == 3:
                count_tiles = world.count_tile_type(2)
                if count_tiles < 2:
                    world.world_map[row][column].set_tile(2)

    ##  ----- NO BLIT ZONE END  ----- ##

    ## FILL SCREEN, and BLIT here ##
    screen.fill((r, g, b))

    world.draw_world(screen)
    screen.blit(save_button.image, save_button.rect)
    screen.blit(load_button.image, load_button.rect)
    screen.blit(save_file_message, (1000, 30))
    pygame.draw.rect(screen, text_box_color, text_box, 3)
    screen.blit(file_name_message, (1008, 65))

    pygame.display.update()
    ## END OF WHILE LOOP

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()