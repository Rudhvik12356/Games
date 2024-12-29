# import pgzrun, random

# WIDTH = 800
# HEIGHT = 600

# speed = 10

# gameState = "play"

# SHAPES = ["circle", "rectangle", "square", "triangle"]
# currentLevel = 1
# shapes = []
# animations = []

# def draw():
#     screen.clear()
#     screen.blit("bground", (0,0))
          
#     if gameState == "win":
#         screen.draw.text("You win!", fontsize = 30, center = (WIDTH/2, HEIGHT/2), color = "lime") 
#     elif gameState == "lose":
#         screen.draw.text("Game Over! Try the level again", fontsize = 30, center = (WIDTH/2, HEIGHT/2), color = "red")
#     elif gameState == "play":
#         for i in shapes:
#             i.draw()   
    
# def update():
#     global shapes
#     if len(shapes) == 0:
#        makeShapes(currentLevel)
       
# def makeShapes(noOfShapes):
#     requiredShapes = getOptionToCreate(noOfShapes)
#     createObjects = createShapes(requiredShapes)
#     posShapes(createObjects)
#     animateShapes(createObjects)
#     return createObjects

# def getOptionToCreate(noOfShapes):
#     createObjects = ["square"]   
#     for i in range(noOfShapes):
#         createObjects.append(random.choice(SHAPES))
#     return createObjects

# def createShapes(createObjects):
#     newShapes = []
#     for i in createObjects:
#         object = Actor(i)
#         newShapes.append(object)
#     return newShapes

# def posShapes(newShapes):
#     noOfGaps = len(newShapes) + 1
#     gapSize = WIDTH/noOfGaps
#     random.shuffle(newShapes)
    
#     for i, shape in enumerate(newShapes):
#         xpos = (i+1)*gapSize
#         shape.x = xpos

# def animateShapes(newShapes):
#     global animations
    
#     for i in newShapes:
#         duration = speed - currentLevel
#         i.anchor = ("center", "bottom")
#         animation = animate(i, duration = duration, on_finished = gameOver, y = HEIGHT)
#         animations.append(animation)
        
# def gameOver():
#     print("Game Over!")
                     
# pgzrun.go()                   
        