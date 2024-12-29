import pgzrun, random

WIDTH = 800
HEIGHT = 600

speed = 10

ITEMS = ["battery", "bag", "chips", "bottle"]

gameState = "play"

currentLevel = 1
items = []
animations = []

def draw():
    screen.clear()
    screen.blit("bground", (0,0))
    
    if gameState == "win":
        screen.draw.text("You win!", fontsize = 30, center = (WIDTH/2, HEIGHT/2), color = "white") 
    elif gameState == "lose":
        screen.draw.text("Game Over! Try the level again", fontsize = 30, center = (WIDTH/2, HEIGHT/2), color = "white")
    elif gameState == "play":
        for i in items:
            i.draw()     

def update():
    global items
    if len(items) == 0:
        items = makeItems(currentLevel) 
    print(items)
    
def makeItems(noOfItems):
    #print("hello")
    requiredItems = getOptionToCreate(noOfItems)
    createObjects = createItems(requiredItems)
    posItems(createObjects)
    animateItems(createObjects)
    return createObjects

def getOptionToCreate(noOfItems):
    createObjects = ["paper"]   
    for i in range(noOfItems):
        createObjects.append(random.choice(ITEMS))
    return createObjects

def createItems(createObjects):
    newItems = []
    for i in createObjects:
        object = Actor(i+"img")
        newItems.append(object)
    return newItems

def posItems(newItems):
    noOfGaps = len(newItems) + 1
    gapSize = WIDTH/noOfGaps
    random.shuffle(newItems)
    
    for i, item in enumerate(newItems):
        xpos = (i+1)*gapSize
        item.x = xpos

def animateItems(newItems):
    global animations
    
    for i in newItems:
        duration = speed - currentLevel
        i.anchor = ("center", "bottom")
        animation = animate(i, duration = duration, on_finished = gameOver, y = HEIGHT)
        animations.append(animation)
     
def on_mouse_down(pos):
    global items, currentLevel
    
    for i in items:
        if i.collidepoint(pos):
            if "paper" in i.image:
                handleGameComplete()
            else:
                gameOver()            

def handleGameComplete():
    global currentLevel, items, gameState, animations
    stopAnimations(animations)
    
    if currentLevel == 6:
        gameState = "win"
    else:
        currentLevel += 1
        items = []
        animations = []        
    
def stopAnimations(animations):
    for a in animations:
        if a.running:
            a.stop()
               
def gameOver():
    global gameState
    print("Game Over!")
    gameState = "lose"
                   
pgzrun.go()            