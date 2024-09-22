import turtle

# Function to draw a rectangle (useful for table, cake, and legs)
def draw_rectangle(width, height, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

# Function to draw a circle (useful for cake decorations)
def draw_circle(radius, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

# Function to draw the table with 2 front legs
def draw_table(table_size, table_color):
    # Draw the tabletop
    turtle.penup()
    turtle.goto(-table_size / 2, -table_size / 4)  # Start drawing from center-bottom
    turtle.pendown()
    draw_rectangle(table_size, table_size / 10, table_color)  # Draw the table

    # Draw the front two legs (ignoring back legs)
    leg_height = table_size / 4
    leg_width = table_size / 20
    
    # Draw front-left leg
    turtle.penup()
    turtle.goto(-table_size / 2, -table_size / 4 - leg_height)  # Position for front-left leg
    turtle.pendown()
    draw_rectangle(leg_width, leg_height, table_color)  # Draw the leg
    
    # Draw front-right leg
    turtle.penup()
    turtle.goto(table_size / 2 - leg_width, -table_size / 4 - leg_height)  # Position for front-right leg
    turtle.pendown()
    draw_rectangle(leg_width, leg_height, table_color)  # Draw the leg

# Function to draw the cake, properly touching the table
def draw_cake(cake_size):
    # Adjust the y-coordinate so the cake rests perfectly on the table
    cake_base_y = -table_size / 4 + table_size / 10
    turtle.penup()
    turtle.goto(-cake_size / 2, cake_base_y)  # Position cake exactly on the table
    turtle.pendown()
    draw_rectangle(cake_size, cake_size / 2, 'pink')  # Cake is pink
    
    # Cake decoration (small circles on top)
    cherry_y = cake_base_y + cake_size / 2
    turtle.penup()
    turtle.goto(-cake_size / 4, cherry_y)
    turtle.pendown()
    draw_circle(cake_size / 10, 'red')  # Cherry-like decoration
    
    turtle.penup()
    turtle.goto(cake_size / 4, cherry_y)
    turtle.pendown()
    draw_circle(cake_size / 10, 'red')  # Another cherry
    
    # Draw a candle in the middle of the cake
    draw_candle(cake_size, cake_base_y)

# Function to draw the candle
def draw_candle(cake_size, cake_base_y):
    # Draw the candle (rectangle)
    candle_y = cake_base_y + cake_size / 2
    turtle.penup()
    turtle.goto(-cake_size / 20, candle_y)
    turtle.pendown()
    draw_rectangle(cake_size / 10, cake_size / 5, 'blue')  # Blue candle
    
    # Draw the flame (circle)
    flame_y = candle_y + cake_size / 5
    turtle.penup()
    turtle.goto(0, flame_y)
    turtle.pendown()
    draw_circle(cake_size / 20, 'yellow')  # Yellow flame

# Function to set up the turtle canvas size
def setup_canvas():
    turtle.setup(600, 600)  # Set the screen size
    turtle.speed(5)  # Slow down the drawing speed for better visualization
    turtle.bgcolor("lightblue")  # Background color

# Main function to run the program
def main():
    setup_canvas()

    # Get user inputs
    global table_size  # Global variable to pass to the cake drawing function
    table_size = int(input("Please enter the length of one side of a table (between 10-100): "))
    table_color = input("Please enter the color of the table: ")
    cake_size = int(input(f"Please enter the size of the cake (between 10-{table_size}): "))
    
    print("Your cake is loading! Happy Birthday!")
    
    # Draw table and cake
    draw_table(table_size, table_color)  # Draw the table with front legs only
    draw_cake(cake_size)  # Draw the cake directly on top of the table
    
    # End the program and wait for user to close the window
    print("Press any key to exit...")
    turtle.done()

# Run the main function
main()