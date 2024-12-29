import pgzrun

TITLE = "The QUIZ GAME"
WIDTH = 900
HEIGHT = 700

score = 0
timer = 10
questionFile = "questions.txt"

marqueeMessage = ""
gameState = "play"

marqueeBox = Rect(0,0, 870, 80)
questionBox = Rect(0,0, 650, 150)
timerBox = Rect(0,0, 150, 150)
skipBox = Rect(0,0, 150, 300)
answerBox1 = Rect(0,0, 300, 150)
answerBox2 = Rect(0,0, 300, 150)
answerBox3 = Rect(0,0, 300, 150)
answerBox4 = Rect(0,0, 300, 150)

answerBox = [answerBox1, answerBox2, answerBox3, answerBox4]
questions = []
questionCount = 0
questionIndex = 0

marqueeBox.move_ip(0,0)
questionBox.move_ip(20, 100)
timerBox.move_ip(700, 100)
skipBox.move_ip(700, 270)
answerBox1.move_ip(20, 270)
answerBox2.move_ip(370, 270)
answerBox3.move_ip(20 ,450)
answerBox4.move_ip(370, 450)

def readQuestionFile():
    global questionCount, questions
    
    question_file = open(questionFile, "r")
    
    for i in question_file:
        questions.append(i)
        questionCount += 1
    question_file.close()    

def readNextQuestion():
    global questionIndex
    questionIndex += 1
    
    return questions.pop(0).split(",")     

pgzrun.go()