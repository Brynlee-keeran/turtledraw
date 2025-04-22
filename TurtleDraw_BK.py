import turtle
import math

print('TurtleDraw Starting...')

screen = turtle.Screen()
screen.setup(width=450, height=450)
screen.title("TurtleDraw_BK")

t = turtle.Turtle()
t.speed(0)
t.penup()

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

filename = input("Enter the name of the input file:")

total_distance = 0
last_pos = None

try: 
    with open(filename, "r") as tddata:
        for line in tddata:

            line = line.strip()
            print (line)

            if not line:
                 continue

            if line.lower() == "stop":
                 t.penup()
                 last_pos = None
                 continue
            
            parts = line.split()
            print(parts)

            if len(parts) == 3:
                 color, x_str, y_str = parts
                 x, y = int(x_str), int(y_str,)

                 t.color(color)
                 t.goto(x, y)

                 if last_pos is not None:
                      dist = math.dist(last_pos, (x, y))
                      total_distance += dist

                 t.pendown()
                 last_pos = (x, y)

except FileNotFoundError:
       print(f"File '{filename}' not found. Please make sure the file exists in the same folder.")
       screen.bye()
       exit()

writer.goto(30, -200)
writer.write(f"Total Distance: {round(total_distance, 2)}", font=("Arial", 12, "normal"))

input("Drawing complete! Press Enter to close the window.")
screen.bye()