import turtle
import random
import math
import time

#WHAT'S NEW?
"""
1.8: Puse Screen Added
"""



#RREGISTER THE SHAPES
turtle.register_shape(r'Assets/SpaceInvaders-Enemy.gif')
turtle.register_shape(r'Assets/SpaceInvaders-Player.gif')
turtle.register_shape(r'Assets/SpaceInvaders-Heart.gif')
turtle.register_shape(r'Assets/SpaceInvaders-PauseButton.gif')
turtle.register_shape(r'Assets/SpaceInvaders-GreyColor.gif')



#Create Main Screen
main_screen = turtle.Screen()
main_screen.bgcolor('black')
main_screen.title('Space Invaders')


#Create Border
main_border_pen = turtle.Turtle()
main_border_pen.speed(0)
main_border_pen.color('white')
main_border_pen.penup()
main_border_pen.goto(-300, -300)
main_border_pen.pendown()
main_border_pen.pensize(3)
for side in range(4):
    main_border_pen.forward(600)
    main_border_pen.left(90)
main_border_pen.hideturtle()


#Create Version
version = 1.6
version_pen = turtle.Turtle()
version_pen.speed(0)
version_pen.color('white')
version_pen.penup()
version_pen.goto(300, -300)
version_string = "Version {}".format(version)
version_pen.write(version_string, move=False, align="right", font=("Arial", 6, "normal"))
version_pen.hideturtle()


#Create 'Score and Heart' Box
box_pen = turtle.Turtle()
box_pen.speed(0)
box_pen.color('white')
box_pen.penup()
box_pen.goto(-200, 300)
box_pen.pendown()
box_pen.begin_fill()
for i in range(2):
    box_pen.right(90)
    box_pen.forward(50)
    box_pen.right(90)
    box_pen.forward(100)
box_pen.color('black')
box_pen.end_fill()
box_pen.hideturtle()


#Create The Score
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color('white')
score_pen.penup()
score_pen.goto(-290, 277)
score_string = "Score: {}".format(score)
score_pen.write(score_string, move=False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()


#Create The Hearts
number_of_hearts = 3
hearts = []
for i in range(number_of_hearts):
    hearts.append(turtle.Turtle())
heartXPos = -280
for heart in hearts:
    heart.shape('Assets/SpaceInvaders-Heart.gif')
    heart.penup()
    heart.speed(0)
    heart.goto(heartXPos, 265)
    heartXPos += 30


#Create Bonus Hearts
bonus_heart_score = 100
bonus_heart_speed = 7
bonus_heart = turtle.Turtle()
bonus_heart.shape(r'Assets/SpaceInvaders-Heart.gif')
bonus_heart.penup()
bonus_heart.speed(0)
bonus_heart.hideturtle()


#Create The Player
player = turtle.Turtle()
player.shape(r'Assets/SpaceInvaders-Player.gif')
player.penup()
player.speed(0)
player.goto(0, -250)
player_speed = 15


#Create The Player's Bullets
player_bullet_state = 'ready'
player_bullet = turtle.Turtle()
player_bullet.speed(0)
player_bullet.color('yellow')
player_bullet.shape('triangle')
player_bullet.penup()
player_bullet.setheading(90)
player_bullet.shapesize(0.5, 0.5)
player_bullet.hideturtle()
player_bullet_speed = 20


#Create The Enemies
number_of_enemies = 5
enemies = []
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())
for enemy in enemies:
    enemy.shape(r'Assets/SpaceInvaders-Enemy.gif')
    enemy.penup()
    enemy.speed(0)
    random_xpos = random.randint(-200, 200)
    random_ypos = random.randint(100,235)
    enemy.goto(random_xpos, random_ypos)
enemy_speed = 10


#Create Pause Screen
pause_screen = turtle.Turtle()
pause_screen.shape(r'Assets/SpaceInvaders-GreyColor.gif')
pause_screen.hideturtle()


#Create The Pause Icon
paused = False
esc_state = True
pause_icon = turtle.Turtle()
pause_icon.shape(r'Assets/SpaceInvaders-PauseButton.gif')
pause_icon.hideturtle()


#Define The Rankup Score
rankup_score = 100



#GAME CONTROLS
def playerMoveLeft():
    xPos = player.xcor()
    xPos -= player_speed
    if xPos < -280:
        xPos = -280
    player.setx(xPos)

def playerMoveRight():
    xPos = player.xcor()
    xPos += player_speed
    if xPos > 280:
        xPos = 280
    player.setx(xPos)

def playerFireBullet():
    global player_bullet_state
    enemy = random.choice(enemies)
    if player_bullet_state == 'ready':
        player_bullet_state = 'fire'
        xPos = player.xcor()
        yPos = player.ycor()
        player_bullet.goto(xPos, yPos + 10)
        player_bullet.showturtle()

def pauseScreen():
    global esc_state
    global paused
    if esc_state == True:
        pause_icon.showturtle()
        esc_state = False
        paused = True
    elif esc_state == False:
        pause_icon.hideturtle()
        esc_state = True
        paused = False

def OnCollision(t1, t2):
    t1XPos = t1.xcor()
    t1YPos = t1.ycor()
    t2XPos = t2.xcor()
    t2YPos = t2.ycor()
    distance = math.sqrt(pow(t1XPos - t2XPos, 2) + pow(t1YPos - t2YPos, 2))
    if distance < 15:
        return True
    else:
        return False



#KEYBOARD BINDINGS
turtle.listen()
turtle.onkey(playerMoveLeft, 'Left')
turtle.onkey(playerMoveRight, 'Right')
turtle.onkey(playerFireBullet, 'space')
turtle.onkey(pauseScreen, 'Escape')



#MAIN GAME LOOP
while True:
    if not paused:

        #ENEMY SETTINGS
        for enemy in enemies:
            #Move The Enemy
            xPos = enemy.xcor()
            xPos += enemy_speed
            enemy.setx(xPos)
            #Move The Enemy Back and Down
            if enemy.xcor() > 280 or enemy.xcor() < -280:
                # todo make the enemies individual
                for e in enemies:
                    yPos = e.ycor()
                    yPos -= 40
                    e.sety(yPos)
                enemy_speed *= -1

            #Collision Player Bullet With The Enemy
            if OnCollision(player_bullet, enemy):
                #Reset The Bullet
                player_bullet.hideturtle()
                player_bullet_state = 'ready'
                player_bullet.goto(0, -400)
                #Reset The Enemy
                random_xpos = random.randint(-200, 200)
                enemy.goto(random_xpos, 235)
                #Change The Score
                score += 10
                score_string = "Score: {}".format(score)
                score_pen.clear()
                score_pen.write(score_string, move=False, align="left", font=("Arial", 14, "normal"))


            #Collision Enemy With The Player
            if OnCollision(player, enemy) or enemy.ycor() < -280:
                number_of_hearts -= 1
                random_xpos = random.randint(-200, 200)
                enemy.goto(random_xpos, 100)
                for h in hearts:
                    h.hideturtle()
                for j in range(number_of_hearts):
                    hearts[j].showturtle()


        #BONUS HEART SETTINGS
        #Spawn and Drop Bonus Hearts
        if score == bonus_heart_score:
            random_xpos = random.randint(-200, 200)
            bonus_heart.goto(random_xpos, 235)
            bonus_heart.showturtle()
            bonus_heart_score += 100
            pass
        yPos = bonus_heart.ycor()
        yPos -= 10
        bonus_heart.sety(yPos)

        #Collision Bonus Heart With Player
        if OnCollision(bonus_heart, player):
            bonus_heart.hideturtle()
            number_of_hearts += 1
            if number_of_hearts < 3:
                for h in hearts:
                    h.hideturtle()
                for j in range(number_of_hearts):
                    hearts[j].showturtle()
            if number_of_hearts > 3:
                number_of_hearts = 3

        #Hide Bonuse Hearts When Out of Bounds
        if bonus_heart.ycor() < -280:
            bonus_heart.hideturtle()


        #RANKUP SETTINGS
        #When The Score For Bonuses Increases 100, Increase Everythings Speed
        if score == rankup_score:
            enemy_speed += 1
            player_bullet_speed += 0.5
            rankup_score += 100
            pass


        #PLAYER BULLET SETTINGS
        #Move The Player Bullet
        if player_bullet_state == 'fire':
            yPos = player_bullet.ycor()
            yPos += player_bullet_speed
            player_bullet.sety(yPos)

        if player_bullet.ycor() > 275:
            player_bullet.hideturtle()
            player_bullet_state = 'ready'


        #GAME OVER SETTINGS
        if number_of_hearts <= 0:
            #Create The Game Over Screen
            game_over_pen = turtle.Turtle()
            game_over_pen.speed(0)
            game_over_pen.color('red')
            game_over_pen.penup()
            game_over_pen.goto(0, 0)
            game_over_pen.write("GAME OVER!", move=False, align="center", font=("Arial", 60, "bold"))
            game_over_pen.hideturtle()
            #Reset The Score
            score_pen.clear()
            score_pen.goto(0, -40)
            score_pen.write(score_string, move=False, align='center', font=("Arial", 20, "normal"))
            score_pen.hideturtle()
            #Reset The Player
            player.hideturtle()
            #Reset The Enemies
            for e in enemies:
                e.hideturtle()
            #Reset The Hearts
            for h in hearts:
                h.hideturtle()
                break
            #Reset The Players Bullet
            player_bullet.hideturtle()



    elif paused:
        enemy.goto(enemy.xcor(), enemy.ycor())
        player.goto(player.xcor(), player.ycor())
        player_bullet.goto(player_bullet.xcor(), player_bullet.ycor())




















#Done
turtle.done()
