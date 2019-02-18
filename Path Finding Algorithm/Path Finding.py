import pygame
import math

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
done = False
clock = pygame.time.Clock()
box_font = pygame.font.SysFont("arial", 11)
total_font = pygame.font.SysFont("arialblack", 15)

# PyGame image function(optional)
_image_library = {}

solving = False
designing = True
background = True
find_start_end = True
squares_dictionary = {}


current_square_x = 3
current_square_y = 2
end_square_x = 2
end_square_y = 3
start_square_x = 1
start_square_y = 1
fps = 200
key = pygame.image.load("Key.png")

# Game Loop
while not done:
    # Quit Function
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Put code here
    if designing is True:
        fps = 200
        """
        Draw the grid, and create a dictionary with all the co-ordinates of the squares, with the value of 0
        """
        while background is True:
            x = 50
            y = 50
            pygame.draw.rect(screen, [255, 255, 255], [0, 0, 1920, 1080])
            background = False
            for i in range(0, 38):
                pygame.draw.line(screen, [0, 0, 0], [x, 0], [x, 1080], 2)
                x += 50
            for i in range(0, 21):
                pygame.draw.line(screen, [0, 0, 0], [0, y], [1920, y], 2)
                y += 50
            for i in range(1, 40):
                for t in range(1, 22):
                    squares_dictionary[str(i) + ", " + str(t)] = 0
            # Draw Border
            pygame.draw.line(screen, [0, 0, 0], [0, 0], [0, 1080], 2)
            pygame.draw.line(screen, [0, 0, 0], [0, 0], [1920, 0], 2)
            pygame.draw.line(screen, [0, 0, 0], [1920, 1080], [0, 1080], 2)
            pygame.draw.line(screen, [0, 0, 0], [1920, 1080], [1920, 0], 2)

        """
        Set mouse monitoring variables
        """
        mouse_event = pygame.mouse.get_pressed()
        mouse_position = pygame.mouse.get_pos()
        mouse_x = mouse_position[0]
        mouse_y = mouse_position[1]

        """
        Check each square and if mouse 1 is clicked set that squares value to 1, or if mouse 2 is clicked set it back to 0
        """
        for i in range(0, 1950, 50):
            for x in range(i, (i + 50)):
                if mouse_x == x:
                    for y in range(0, 1050, 50):
                        for t in range(y, (y + 50)):
                            if mouse_y == t:
                                if mouse_event == (1, 0, 0):
                                    if i == 0:
                                        x_clicked = 1
                                    else:
                                        x_clicked = (i / 50) + 1

                                    if y == 0:
                                        y_clicked = 1
                                    else:
                                        y_clicked = (y / 50) + 1

                                    clicked_square = str(x_clicked) + ", " + str(y_clicked)
                                    # print clicked_square
                                    squares_dictionary[clicked_square] = 1

                                elif mouse_event == (0, 0, 1):
                                    if i == 0:
                                        x_clicked = 1
                                    else:
                                        x_clicked = (i / 50) + 1

                                    if y == 0:
                                        y_clicked = 1
                                    else:
                                        y_clicked = (y / 50) + 1

                                    clicked_square = str(x_clicked) + ", " + str(y_clicked)
                                    # print clicked_square
                                    squares_dictionary[clicked_square] = 0

        """
        If the 1 or 2 key is being held down place the start or end point
        """
        if pygame.key.get_pressed()[pygame.K_1] or pygame.key.get_pressed()[pygame.K_2]:
            for i in range(0, 1950, 50):
                for x in range(i, (i + 50)):
                    if mouse_x == x:
                        for y in range(0, 1050, 50):
                            for t in range(y, (y + 50)):
                                if mouse_y == t:
                                    if mouse_event == (1, 0, 0):
                                        if i == 0:
                                            x_clicked = 1
                                        else:
                                            x_clicked = (i / 50) + 1

                                        if y == 0:
                                            y_clicked = 1
                                        else:
                                            y_clicked = (y / 50) + 1

                                        clicked_square = str(x_clicked) + ", " + str(y_clicked)
                                        # print clicked_square
                                        if pygame.key.get_pressed()[pygame.K_1]:
                                            squares_dictionary[clicked_square] = 2
                                        elif pygame.key.get_pressed()[pygame.K_2]:
                                            squares_dictionary[clicked_square] = 3

        """
        Iterate through the squares and if there dictionary value is 1 set them to green, or value 0 clear them, or value 2 set to blue, or value 4, set to red
        """
        for i in range(1, 40):
            for t in range(1, 22):
                if squares_dictionary[str(i) + ", " + str(t)] == 1:
                    pygame.draw.rect(screen, [0, 255, 0], [((i - 1) * 50) + 2, ((t - 1) * 50) + 2, 48, 48])

                elif squares_dictionary[str(i) + ", " + str(t)] == 0:
                    pygame.draw.rect(screen, [255, 255, 255], [((i - 1) * 50) + 2, ((t - 1) * 50) + 2, 48, 48])

                elif squares_dictionary[str(i) + ", " + str(t)] == 2:
                    pygame.draw.rect(screen, [0, 0, 255], [((i - 1) * 50) + 2, ((t - 1) * 50) + 2, 48, 48])

                elif squares_dictionary[str(i) + ", " + str(t)] == 3:
                    pygame.draw.rect(screen, [255, 0, 0], [((i - 1) * 50) + 2, ((t - 1) * 50) + 2, 48, 48])

        """
        Draw key
        """
        screen.blit(key, (1610, 13))
        if pygame.key.get_pressed()[pygame.K_3]:
            designing = False
            solving = True
            for i in range(1, 40):
                for t in range(1, 22):
                    if squares_dictionary[str(i) + ", " + str(t)] == 0:
                        squares_dictionary[str(i) + ", " + str(t)] = 99999

    elif solving is True:
        fps = 20000
        if find_start_end is True:
            for i in range(1, 40):
                for t in range(1, 22):
                    if squares_dictionary[str(i) + ", " + str(t)] == 2:
                        current_square_x = i
                        current_square_y = t
                        start_square_x = i
                        start_square_y = t

                    elif squares_dictionary[str(i) + ", " + str(t)] == 3:
                        end_square_x = i
                        end_square_y = t
                        squares_dictionary[str(start_square_x) + ", " + str(start_square_y)] = 99998
                        squares_dictionary[str(end_square_x) + ", " + str(end_square_y)] = 99998
            find_start_end = False
            for i in squares_dictionary:
                if squares_dictionary[i] == 1:
                    squares_dictionary[i] = 99997


        #distance_to_end = math.sqrt(((end_square_x - current_square_x) * (end_square_x - current_square_x)) + ((end_square_y - current_square_y) * (end_square_y - current_square_y)))
        # print distance_to_end
        distance_from_start = math.sqrt(((start_square_x - current_square_x) * (start_square_x - current_square_x)) + ((start_square_y - current_square_y) * (start_square_y - current_square_y)))
        # print distance_from_start

        # Draw Right
        print squares_dictionary
        if squares_dictionary[str(current_square_x + 1) + ", " + str(current_square_y - 0)] == 99999:
            pygame.draw.rect(screen, [255, 255, 0], [((current_square_x + 0) * 50) + 2, ((current_square_y - 1) * 50) + 2, 48, 48])
            print str(current_square_x + 1) + ", " + str(current_square_y - 0)
            right_h = math.sqrt(((end_square_x - (current_square_x + 1)) * (end_square_x - (current_square_x + 1))) + ((end_square_y - (current_square_y + 0)) * (end_square_y - (current_square_y + 0))))
            right_g = math.sqrt(((start_square_x - (current_square_x + 1)) * (start_square_x - (current_square_x + 1))) + ((start_square_y - (current_square_y + 0)) * (start_square_y - (current_square_y + 0))))
            right_f = right_g + right_h

            squares_dictionary[str((current_square_x + 1)) + ", " + str(current_square_y)] = right_f

            # print right_h
            # print right_g
            right_h_text = box_font.render(str(round(right_h, 2)), False, (0, 0, 0))
            right_g_text = box_font.render(str(round(right_g, 2)), False, (0, 0, 0))
            right_f_text = total_font.render(str(round(right_f, 3)), False, (0, 0, 0))

            screen.blit(right_h_text, ((((current_square_x + 0) * 50) + 27), (((current_square_y - 1) * 50) + 1)))
            screen.blit(right_g_text, ((((current_square_x + 0) * 50) + 27), (((current_square_y - 1) * 50) + 12)))
            screen.blit(right_f_text, ((((current_square_x + 0) * 50) + 5), (((current_square_y - 1) * 50) + 25)))

        # Draw Left
        if squares_dictionary[str(current_square_x - 1) + ", " + str(current_square_y - 0)] == 99999:
            pygame.draw.rect(screen, [255, 255, 0], [((current_square_x - 2) * 50) + 2, ((current_square_y - 1) * 50) + 2, 48, 48])
            left_h = math.sqrt(((end_square_x - (current_square_x - 1)) * (end_square_x - (current_square_x - 1))) + ((end_square_y - (current_square_y + 0)) * (end_square_y - (current_square_y + 0))))
            left_g = math.sqrt(((start_square_x - (current_square_x - 1)) * (start_square_x - (current_square_x - 1))) + ((start_square_y - (current_square_y + 0)) * (start_square_y - (current_square_y + 0))))
            left_f = left_h + left_g

            squares_dictionary[str((current_square_x - 1)) + ", " + str(current_square_y)] = left_f

            # print left_h
            # print left_g
            left_h_text = box_font.render(str(round(left_h, 2)), False, (0, 0, 0))
            left_g_text = box_font.render(str(round(left_g, 2)), False, (0, 0, 0))
            left_f_text = total_font.render(str(round(left_f, 2)), False, (0, 0, 0))

            screen.blit(left_h_text, ((((current_square_x - 2) * 50) + 27), (((current_square_y - 1) * 50) + 1)))
            screen.blit(left_g_text, ((((current_square_x - 2) * 50) + 27), (((current_square_y - 1) * 50) + 12)))
            screen.blit(left_f_text, ((((current_square_x - 2) * 50) + 5), (((current_square_y - 1) * 50) + 25)))

        # Draw Top
        if squares_dictionary[str(current_square_x + 0) + ", " + str(current_square_y - 1)] == 99999:
            pygame.draw.rect(screen, [255, 255, 0], [((current_square_x - 1) * 50) + 2, ((current_square_y - 2) * 50) + 2, 48, 48])
            top_h = math.sqrt(((end_square_x - (current_square_x + 0)) * (end_square_x - (current_square_x + 0))) + ((end_square_y - (current_square_y - 1)) * (end_square_y - (current_square_y - 1))))
            top_g = math.sqrt(((start_square_x - (current_square_x + 0)) * (start_square_x - (current_square_x + 0))) + ((start_square_y - (current_square_y - 1)) * (start_square_y - (current_square_y - 1))))
            top_f = top_h + top_g

            squares_dictionary[str(current_square_x) + ", " + str((current_square_y - 1))] = top_f

            # print top_h
            # print top_g
            top_h_text = box_font.render(str(round(top_h, 2)), False, (0, 0, 0))
            top_g_text = box_font.render(str(round(top_g, 2)), False, (0, 0, 0))
            top_f_text = total_font.render(str(round(top_f, 2)), False, (0, 0, 0))

            screen.blit(top_h_text, ((((current_square_x - 1) * 50) + 27), (((current_square_y - 2) * 50) + 1)))
            screen.blit(top_g_text, ((((current_square_x - 1) * 50) + 27), (((current_square_y - 2) * 50) + 12)))
            screen.blit(top_f_text, ((((current_square_x - 1) * 50) + 5), (((current_square_y - 2) * 50) + 25)))

        # Draw Bottom
        if squares_dictionary[str(current_square_x + 0) + ", " + str(current_square_y + 1)] == 99999:
            pygame.draw.rect(screen, [255, 255, 0], [((current_square_x - 1) * 50) + 2, ((current_square_y + 0) * 50) + 2, 48, 48])
            bottom_h = math.sqrt(((end_square_x - (current_square_x + 0)) * (end_square_x - (current_square_x + 0))) + ((end_square_y - (current_square_y + 1)) * (end_square_y - (current_square_y + 1))))
            bottom_g = math.sqrt(((start_square_x - (current_square_x + 0)) * (start_square_x - (current_square_x + 0))) + ((start_square_y - (current_square_y + 1)) * (start_square_y - (current_square_y + 1))))
            bottom_f = bottom_h + bottom_g

            squares_dictionary[str(current_square_x) + ", " + str((current_square_y + 1))] = bottom_f

            # print bottom_h
            # print bottom_g

            bottom_h_text = box_font.render(str(round(bottom_h, 2)), False, (0, 0, 0))
            bottom_g_text = box_font.render(str(round(bottom_g, 2)), False, (0, 0, 0))
            bottom_f_text = total_font.render(str(round(bottom_f, 2)), False, (0, 0, 0))

            screen.blit(bottom_h_text, ((((current_square_x - 1) * 50) + 27), (((current_square_y + 0) * 50) + 1)))
            screen.blit(bottom_g_text, ((((current_square_x - 1) * 50) + 27), (((current_square_y + 0) * 50) + 12)))
            screen.blit(bottom_f_text, ((((current_square_x - 1) * 50) + 5), (((current_square_y + 0) * 50) + 25)))


        #end_distance_text = box_font.render(str(bottom_h), True, (0, 0, 0))
        #screen.blit(end_distance_text, ()

        

        lowest = min(squares_dictionary, key=squares_dictionary.get)
        print lowest
        split = lowest.split(", ")
        test1, test2 = split

        new_x = int(test1)
        new_y = int(test2)

        if squares_dictionary[str(new_x + 1) + ", " + str(new_y - 0)] == 99999 or squares_dictionary[str(new_x - 1) + ", " + str(new_y - 0)] == 99999 or squares_dictionary[str(new_x + 0) + ", " + str(new_y - 1)] == 99999 or squares_dictionary[str(new_x + 0) + ", " + str(new_y + 1)] == 99999:
            current_square_x = new_x
            current_square_y = new_y
        else:
            squares_dictionary[str(new_x) + ", " + str(new_y)] = 99996

    pygame.display.flip()
    clock.tick(fps)
