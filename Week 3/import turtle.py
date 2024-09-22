import turtle

# Function to draw a rectangle (useful for table and cake)
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

# Function to draw the table
def draw_table(table_size, table_color):
    turtle.penup()
    turtle.goto(-table_size / 2, -table_size / 4)  # Start drawing from center-bottom
    turtle.pendown()
    draw_rectangle(table_size, table_size / 2, table_color)  # Draw the table

def draw_table_legs(table_size, table_color):
    turtle.penup()
    turtle.goto(-table_size / 2, -table_size / 4)  # Start drawing from center-bottom
    turtle.left(90)
    turtle.pendown()
    draw_rectangle(table_size, table_size / 2, table_color)  # Draw the table

# Function to draw the cake
def draw_cake(cake_size):
    # Cake base
    turtle.penup()
    turtle.goto(-cake_size / 2, 0)  # Position cake on the table
    turtle.pendown()
    draw_rectangle(cake_size, cake_size / 2, 'pink')  # Cake is pink
    
    # Cake decoration (small circles on top)
    turtle.penup()
    turtle.goto(-cake_size / 4, cake_size / 2)
    turtle.pendown()
    draw_circle(cake_size / 10, 'red')  # Cherry-like decoration
    
    turtle.penup()
    turtle.goto(cake_size / 4, cake_size / 2)
    turtle.pendown()
    draw_circle(cake_size / 10, 'red')  # Another cherry
    
    # Draw a candle in the middle of the cake
    draw_candle(cake_size)

# Function to draw the candle
def draw_candle(cake_size):
    # Draw the candle (rectangle)
    turtle.penup()
    turtle.goto(-cake_size / 20, cake_size / 2)
    turtle.pendown()
    draw_rectangle(cake_size / 10, cake_size / 5, 'blue')  # Blue candle
    
    # Draw the flame (circle)
    turtle.penup()
    turtle.goto(0, cake_size / 2 + cake_size / 5)
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
    table_size = int(input("Please enter the length of one side of a table (between 10-100): "))
    table_color = input("Please enter the color of the table: ")
    cake_size = int(input(f"Please enter the size of the cake (between 10-{table_size}): "))
    leg_size= int(input("enter leg size"))
    
    print("Your cake is loading! Happy Birthday!")
    
    # Draw table and cake

    draw_table(table_size, table_color)
    draw_cake(cake_size)
    
    # End the program and wait for user to close the window
    print("Press any key to exit...")
    turtle.done()

# Run the main function
main()