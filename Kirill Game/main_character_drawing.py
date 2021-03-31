"""This contains all the drawing commands required for
the main character in the game"""

# Import arcade library required for drawings
import arcade

def draw_character(x, y):
    # This function will draw the main character, x and y are starting coordinates
    # Open window
    arcade.open_window(800, 600, "Main Character")

    # Set the background color
    arcade.set_background_color(arcade.csscolor.WHITE)

    # Get ready to draw
    arcade.start_render()

    # Draw Head
    # Hair
    arcade.draw_xywh_rectangle_filled(x + 4, y - 10, 40, 10, arcade.csscolor.BLACK)
    # Head itself
    arcade.draw_xywh_rectangle_filled(x + 4, y - 37, 40, 27, arcade.csscolor.SANDY_BROWN)
    # Mouth
    arcade.draw_xywh_rectangle_filled(x + 30, y - 31, 14, 3, arcade.csscolor.BLACK)
    # Eyes
    arcade.draw_xywh_rectangle_filled(x + 36, y - 18, 8, 5, arcade.csscolor.BLACK)

    # Draw Neck
    arcade.draw_xywh_rectangle_filled(x + 19, y - 44, 11, 7, arcade.csscolor.SANDY_BROWN)

    # Draw Body
    arcade.draw_xywh_rectangle_filled(x + 13, y - 79, 21, 35, arcade.csscolor.INDIANRED)
    arcade.draw_xywh_rectangle_outline(x + 13, y - 79, 21, 35, arcade.csscolor.DARK_GREY, 1)

    # Draw Arms
    # Right Arm
    arcade.draw_xywh_rectangle_filled(x + 22, y - 65, 7, 14, arcade.csscolor.INDIANRED)
    arcade.draw_xywh_rectangle_outline(x + 22, y - 65, 7, 14, arcade.csscolor.DARK_GREY, 1)
    # Left Arm
    arcade.draw_xywh_rectangle_filled(x + 34, y - 57, 14, 6, arcade.csscolor.INDIANRED)
    arcade.draw_xywh_rectangle_outline(x + 34, y - 57, 14, 6, arcade.csscolor.DARK_GREY, 1)
    # Right Hand
    arcade.draw_xywh_rectangle_filled(x + 22, y - 72, 7, 7, arcade.csscolor.BROWN)
    arcade.draw_xywh_rectangle_outline(x + 22, y - 72, 7, 7, arcade.csscolor.DARK_GREY, 1)
    # Left Hand
    arcade.draw_xywh_rectangle_filled(x + 48, y - 57, 4, 6, arcade.csscolor.BROWN)
    arcade.draw_xywh_rectangle_outline(x + 48, y - 57, 4, 6, arcade.csscolor.DARK_GREY, 1)

    # Draw Gun
    arcade.draw_polygon_filled(((x + 52, y - 40),
                                (x + 83, y - 40),
                                (x + 83, y - 46),
                                (x + 60, y - 46),
                                (x + 60, y - 57),
                                (x + 52, y - 57)
                                ),
                               arcade.csscolor.GREY)
    arcade.draw_polygon_outline(((x + 52, y - 40),
                                (x + 83, y - 40),
                                (x + 83, y - 46),
                                (x + 60, y - 46),
                                (x + 60, y - 57),
                                (x + 52, y - 57)
                                ),
                               arcade.csscolor.DARK_GREY, 1)

    # Draw Legs
    # Left Leg
    arcade.draw_xywh_rectangle_filled(x + 13, y - 117, 8, 38, arcade.csscolor.GRAY)
    # Left Shoe
    # Right Leg
    arcade.draw_xywh_rectangle_filled(x + 26, y - 115, 8, 36, arcade.csscolor.GRAY)
    # Right Shoe
    # Between Legs
    arcade.draw_xywh_rectangle_filled(x + 21, y - 88, 5, 9, arcade.csscolor.GRAY)

    # Finish drawing
    arcade.finish_render()

    # Keep the window up until someone closes it.
    arcade.run()

def main():
    draw_character(300, 400)

main()