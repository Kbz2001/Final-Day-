# Warm Up
#--------
# Use Turtle to draw any polygon on the screen.
# Refresher: What is a polygon?
# User enters the length of the sides and how many sides.
# Tip: Angle to turn by is 360/(number of sides)
# Ex. For a Triangle: 360/3 = 120
# Can be done with or without functions
# Try to use event handling! (Must use functions)
# Use loops!

# import turtle

# window = turtle.Screen()
# my_turtle = turtle.Turtle()

# def drawPolygon(length, sides):
#   sides = int(sides)
#   angle = 360/float(sides)

#   for i in range(sides):
#     my_turtle.forward(length)
#     my_turtle.right(angle)

# length_input = input("How long do you want the sides to be? ")
# sides_input = input("How many sides do you want to have? ")
# print("=> Click your \"a\" key in the white box to begin drawing!")

# def drawShape():
#   drawPolygon(length_input, sides_input)

# window.onkey(drawShape, "a")
# window.listen()

# Final Project
# Using Turtle to make a game or make something on the screen. 

# Cube.io

import pygame, sys, time, random

pygame.init()
window = pygame.display_set_mode((500,500)) # Tuple containing 500 and 500
pygame.set_caption("Cube.io Game")

# Tuple in Python: (x, y, z, ...)

# RGB Colors using tuples (red, green, blue)
# RBG Values go from 0 to 255
yellow = (255, 255, 0)
white = (255, 255, 255)
starting_color = (255, 0, 0)
ending_color = (0, 0, 255)

food = [random.randrange(1, 500), random.randrange(1,500), 10, 10]
bad_food = [random.randrange(1, 500), random.randrange(1,500), 10, 10]

speed = 5
cubeX = 250
cubeY = 250
cubeSize = 20

# Start of the game
run = True
while run:
  pygame.time_delay(10)
  window.fill(white)
  food_status = True
  bad_food_status = True

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
      # Stop the game

  # Handling key press events
  keys = pygame.key.get_pressed()

  if keys[pygame.K_RIGHT]:
    if cubeX >= 480:
      cubeX = 480
    else:
      cubeX += speed
  elif keys[pygame.K_LEFT]:
    if cubeX <= 0:
      cubeX = 0
    else:
      cubeX -= speed
  elif keys[pygame.K_UP]:
    if cubeY <= 0:
      cubeY = 0
    else:
      cubeY -= speed
  elif keys[pygame.K_DOWN]:
    if cubeY <= 480:
      cubeY = 480
    else:
      cubeY += speed

  cube = pygame.React(cubeX, cubeY, cubeSize, cubeSize)

  # Draw rectangle
  if cubeSize <= 100:
    pygame.draw.react(window, starting_color, cube)
  else:
    pygame.draw.react(window, ending_color, cube)

  # Check for collision
  if cube.colliderect(food):
    cubeSize += 10
    food_status = False

  if cube.colliderect(bad_food):
    cubeSize -= 10
    bad_food_status = False
  
  # Spawn new food
  if food_status == False:
    food = [random.randrange(1, 500), random.randrange(1,500), 10, 10]
  
  # Spawn in new bad food
  if bad_food_status == False:
    bad_food = [random.randrange(1, 500), random.randrange(1,500), 10, 10]
  
  # Draw food
  pygame.draw.rect(window, ending_color, pygame.Rect(food))

  # Draw bad food
  pygame.draw.rect(window, yellow, pygame.Rect(bad_food))

  pygame.display.update()

pygame.quit()