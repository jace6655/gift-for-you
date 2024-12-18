import turtle
import tkinter as tk
from tkinter import simpledialog
import colorsys

# Set up the screen for Turtle
turtle.speed(5)
turtle.bgcolor("black")
cake_drawn = False  # Flag to check if the cake has been drawn
continue_button_area = (-100, -200, 100, -160)  # Coordinates for the "Continue" button area

# Global variables for name, birth year, and favorite color
name = ""
birth_year = 0
favorite_color = ""

# Function to draw a rectangle (used for the cake base and layers)
def draw_rectangle(color, width, height):
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

# Function to draw candles
def draw_candle(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("yellow")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
    turtle.end_fill()

# Function to draw the flame on top of the candle
def draw_flame(x, y):
    turtle.penup()
    turtle.goto(x + 5, y + 50)  # Position above the candle
    turtle.pendown()
    turtle.color("orange")
    turtle.begin_fill()
    for _ in range(3):  # Flame is a triangle
        turtle.forward(10)
        turtle.left(120)
    turtle.end_fill()

# Function to generate a pastel color palette based on the favorite color
def generate_pastel_palette(base_color):
    h, s, v = colorsys.rgb_to_hsv(base_color[0], base_color[1], base_color[2])
    
    palette = []
    for i in range(5):
        # Generate lighter shades by reducing the saturation and increasing brightness
        new_s = max(0.1, s * (0.7 + i * 0.1))  # Saturation decreases slightly
        new_v = min(1.0, v + i * 0.1)  # Brightness increases slightly
        new_color = colorsys.hsv_to_rgb(h, new_s, new_v)
        palette.append(new_color)
    return palette

# Function to draw the cake with candles
def draw_cake(age, color_palette):
    global cake_drawn
    if cake_drawn:  # If cake is already drawn, do nothing
        return

    # Cake size adjustments based on the number of candles
    cake_width = max(200, age * 20)  # Ensure the cake is wide enough for all candles
    cake_height = 100

    # Cake base
    turtle.penup()
    turtle.goto(-cake_width / 2, -100)  # Position the turtle at the bottom left of the cake
    turtle.pendown()
    draw_rectangle(color_palette[0], cake_width, cake_height)  # Cake base

    # Second layer of the cake
    second_layer_height = 60
    turtle.penup()
    turtle.goto(-cake_width / 2 + 10, 0)  # Position for the second layer
    turtle.pendown()
    draw_rectangle(color_palette[1], cake_width - 20, second_layer_height)  # Second layer

    # Center of the cake
    center_x = 0  # Center of the cake
    spacing = 20  # Default space between candles
    
    # If the number of candles exceeds the cake width, reduce spacing
    max_candles = cake_width // spacing
    if age > max_candles:
        spacing = cake_width // age  # Adjust spacing if there are too many candles

    # Calculate the starting x-coordinate for the first candle so that they are centered
    start_x = center_x - (age - 1) * spacing / 2

    # Draw the candles based on age
    for i in range(age):
        x_pos = start_x + i * spacing
        draw_candle(x_pos, 60)
        draw_flame(x_pos, 60)

    # Add the "Happy Birthday!" text
    turtle.penup()
    turtle.goto(0, 150)  # Position the text
    turtle.pendown()
    turtle.color("white")
    turtle.write(f"Happy Birthday, {name}!", align="center", font=("times new roman", 24, "normal"))

    # Add a "Continue" message below the cake
    turtle.penup()
    turtle.goto(0, -180)  # Position for "Continue" button
    turtle.pendown()
    turtle.color("white")
    turtle.write("Continue", align="center", font=("times new roman", 18, "normal"))

    cake_drawn = True

# Function to display "Click Me" and wait for the first click
def display_click_me():
    turtle.penup()
    turtle.goto(0, 0)  # Position the turtle at the center
    turtle.pendown()
    turtle.color("white")
    turtle.write("Click Me!", align="center", font=("times new roman", 24, "normal"))

# Function to prompt for the name, birthdate, and favorite color
def ask_for_details():
    global name, birth_year, favorite_color

    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window

    # Ask for name
    name = simpledialog.askstring("Name", "What is your name?", parent=root)

    # Ask for birth year
    birth_year = simpledialog.askinteger("Birth Year", "What is your birth year?", parent=root)

    # Ask for favorite color (in RGB format)
    favorite_color_str = simpledialog.askstring("Favorite Color", "What is your favorite color? (e.g., red, blue)", parent=root)

    # Convert the favorite color to RGB (you can map string names to RGB here)
    color_map = {
        "red": (1, 0, 0),
        "green": (0, 1, 0),
        "blue": (0, 0, 1),
        "yellow": (1, 1, 0),
        "purple": (0.5, 0, 0.5),
        "pink": (1, 0.75, 0.8),
        "orange": (1, 0.5, 0),
        "brown": (0.6, 0.4, 0.2),
        "white": (1, 1, 1),
        "black": (0, 0, 0),
    }

    favorite_color = color_map.get(favorite_color_str.lower(), (1, 1, 1))  # Default to white if unknown color
    # Generate the cake's pastel color palette
    color_palette = generate_pastel_palette(favorite_color)

    # Calculate age (2024 - birth year)
    age = 2024 - birth_year

    # Clear the screen and draw the cake with candles based on age and favorite color
    turtle.clear()
    draw_cake(age, color_palette)

# Function to handle the "Click Me" button click
def on_click(x, y):
    global cake_drawn
    # If not drawn yet, show details and draw the cake
    if not cake_drawn:
        turtle.clear()  # Clear the "Click Me" message
        ask_for_details()  # Ask for name, birth year, and favorite color, then draw the cake
    # If the user clicks on the "Continue" button below the cake, show the next page
    elif continue_button_area[0] <= x <= continue_button_area[2] and continue_button_area[1] <= y <= continue_button_area[3]:
        show_final_page()  # Go to the next page after clicking "Continue"

# Function to draw a birthday-themed border around the message
def draw_birthday_border():
    turtle.penup()
    turtle.goto(-250, 200)  # Start at the top left corner of the border
    turtle.pendown()
    turtle.color("yellow")
    
    # Draw a rectangular border
    for _ in range(2):
        turtle.forward(500)  # Width of the border
        turtle.left(90)
        turtle.forward(400)  # Height of the border
        turtle.left(90)

# Function to show the final page with a message and birthday border
def show_final_page():
    turtle.clear()  # Clear the previous drawings
    
    # Add a special birthday message at the center
    turtle.penup()
    turtle.goto(0, 100)
    turtle.pendown()
    turtle.color("green")
    turtle.write(f"Happy {2024 - birth_year}th Birthday, {name}!", align="center", font=("Times new roman", 30, "normal"))

    # Break the long message into smaller chunks and display line by line
    message_parts = [

        "May your day be filled with joy and laughter as you approach adulthood, babiii.",
        "I made this Python program as my present for you because I wanted to combine something practical with something meaningful.",
        "As you step into this new chapter of your life, I thought this would be a fun way to celebrate and inspire your own creativity.",
        "Python is a powerful language that can open doors to endless possibilities, just like the amazing future that lies ahead for you.",

        "Thank you for being who you are, for being born, and for sharing your light with the world.",
        "I’m so grateful to be a part of your journey, and I can’t wait to see everything you will achieve in the years to come.",
        "May your dreams always be within reach and may you continue to grow, not just in age, but in wisdom, kindness, and love.",
        "Here’s to many more birthdays, love, happiness, shared memories, and adventures ahead, lovee! Iloveyouuu!!🫶🏻🫶🏻"
    ]

    # Display each part with some spacing in between
    y_position = 50
    for part in message_parts:
        turtle.penup()
        turtle.goto(0, y_position)
        turtle.pendown()
        turtle.write(part, align="center", font=("times new roman", 15, "normal"))
        turtle.color("white")
        y_position -= 30  # Move down for the next line

# Display "Click Me" text
display_click_me()

# Set up the screen to listen for clicks
turtle.onscreenclick(on_click)

turtle.done()